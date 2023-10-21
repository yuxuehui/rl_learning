#!/usr/bin/env python3

"""
Trains a 2-layer MLP with CAVIA-TRPO.

Usage:

python examples/rl/cavia_trpo.py
"""

import random

import cherry as ch
import gym
import numpy as np
import torch
from cherry.algorithms import a2c, trpo
from cherry.models.robotics import LinearValue
from torch import autograd
from torch.distributions.kl import kl_divergence
from torch.nn.utils import parameters_to_vector, vector_to_parameters
from tqdm import tqdm

import learn2learn as l2l
#!/usr/bin/env python3

import math

import cherry as ch
import torch
from torch import nn
from torch.distributions import Normal, Categorical

EPSILON = 1e-6


def linear_init(module):
    if isinstance(module, nn.Linear):
        nn.init.xavier_uniform_(module.weight)
        module.bias.data.zero_()
    return module


class CaviaDiagNormalPolicy(nn.Module):

    def __init__(self, input_size, output_size, hiddens=None, activation='relu', num_context_params=2, device='cpu'):
        super(CaviaDiagNormalPolicy, self).__init__()
        self.device = device
        if hiddens is None:
            hiddens = [100, 100]
        if activation == 'relu':
            activation = nn.ReLU
        elif activation == 'tanh':
            activation = nn.Tanh
        layers = [linear_init(nn.Linear(input_size+num_context_params, hiddens[0])), activation()]
        for i, o in zip(hiddens[:-1], hiddens[1:]):
            layers.append(linear_init(nn.Linear(i, o)))
            layers.append(activation())
        layers.append(linear_init(nn.Linear(hiddens[-1], output_size)))

        self.num_context_params = num_context_params
        self.context_params = torch.zeros(self.num_context_params, requires_grad=True).to(self.device)

        self.mean = nn.Sequential(*layers).to(self.device)
        self.sigma = nn.Parameter(torch.Tensor(output_size)).to(self.device)
        self.sigma.data.fill_(math.log(1))

    def density(self, state):
        state = state.to(self.device, non_blocking=True)
        # concatenate context parameters to input
        state = torch.cat((state, self.context_params.expand(state.shape[:-1] + self.context_params.shape)),
                          dim=len(state.shape) - 1)

        loc = self.mean(state)
        scale = torch.exp(torch.clamp(self.sigma, min=math.log(EPSILON)))
        return Normal(loc=loc, scale=scale)

    def log_prob(self, state, action):
        density = self.density(state)
        return density.log_prob(action).mean(dim=1, keepdim=True)

    def forward(self, state):

        density = self.density(state)
        action = density.sample()
        return action

    def reset_context(self):
        # torch.zero_(self.context_params)
        self.context_params[:] = 0  # torch.zeros(self.num_context_params, requires_grad=True).to(self.device)

class DiagNormalPolicy(nn.Module):

    def __init__(self, input_size, output_size, hiddens=None, activation='relu', device='cpu'):
        super(DiagNormalPolicy, self).__init__()
        self.device = device
        if hiddens is None:
            hiddens = [100, 100]
        if activation == 'relu':
            activation = nn.ReLU
        elif activation == 'tanh':
            activation = nn.Tanh
        layers = [linear_init(nn.Linear(input_size, hiddens[0])), activation()]
        for i, o in zip(hiddens[:-1], hiddens[1:]):
            layers.append(linear_init(nn.Linear(i, o)))
            layers.append(activation())
        layers.append(linear_init(nn.Linear(hiddens[-1], output_size)))
        self.mean = nn.Sequential(*layers)
        self.sigma = nn.Parameter(torch.Tensor(output_size))
        self.sigma.data.fill_(math.log(1))

    def density(self, state):
        state = state.to(self.device, non_blocking=True)
        loc = self.mean(state)
        scale = torch.exp(torch.clamp(self.sigma, min=math.log(EPSILON)))
        return Normal(loc=loc, scale=scale)

    def log_prob(self, state, action):
        density = self.density(state)
        return density.log_prob(action).mean(dim=1, keepdim=True)

    def forward(self, state):
        density = self.density(state)
        action = density.sample()
        return action


class CategoricalPolicy(nn.Module):

    def __init__(self, input_size, output_size, hiddens=None):
        super(CategoricalPolicy, self).__init__()
        if hiddens is None:
            hiddens = [100, 100]
        layers = [linear_init(nn.Linear(input_size, hiddens[0])), nn.ReLU()]
        for i, o in zip(hiddens[:-1], hiddens[1:]):
            layers.append(linear_init(nn.Linear(i, o)))
            layers.append(nn.ReLU())
        layers.append(linear_init(nn.Linear(hiddens[-1], output_size)))
        self.mean = nn.Sequential(*layers)
        self.input_size = input_size

    def forward(self, state):
        state = ch.onehot(state, dim=self.input_size)
        loc = self.mean(state)
        density = Categorical(logits=loc)
        action = density.sample()
        log_prob = density.log_prob(action).mean().view(-1, 1).detach()
        return action, {'density': density, 'log_prob': log_prob}


def compute_advantages(baseline, tau, gamma, rewards, dones, states, next_states):
    # Update baseline
    returns = ch.td.discount(gamma, rewards, dones)
    baseline.fit(states, returns)
    values = baseline(states)
    next_values = baseline(next_states)
    bootstraps = values * (1.0 - dones) + next_values * dones
    next_value = torch.zeros(1, device=values.device)
    return ch.pg.generalized_advantage(tau=tau,
                                       gamma=gamma,
                                       rewards=rewards,
                                       dones=dones,
                                       values=bootstraps,
                                       next_value=next_value)


def maml_a2c_loss(train_episodes, learner, baseline, gamma, tau):
    # Update policy and baseline
    states = train_episodes.state()
    actions = train_episodes.action()
    rewards = train_episodes.reward()
    dones = train_episodes.done()
    next_states = train_episodes.next_state()
    log_probs = learner.log_prob(states, actions)
    advantages = compute_advantages(baseline, tau, gamma, rewards,
                                    dones, states, next_states)
    advantages = ch.normalize(advantages).detach()
    return a2c.policy_loss(log_probs, advantages)


def fast_adapt_a2c(clone, train_episodes, adapt_lr, baseline, gamma, tau, first_order=False):
    second_order = not first_order
    loss = maml_a2c_loss(train_episodes, clone, baseline, gamma, tau)
    gradients = autograd.grad(loss,
                              clone.context_params,
                              retain_graph=second_order,
                              create_graph=second_order)

    if not first_order:
        clone.context_params = clone.context_params - adapt_lr * gradients[0]
    else:
        clone.context_params = clone.context_params - adapt_lr * gradients[0].detach()

    return l2l.utils.update_module(clone)
    # return l2l.algorithms.maml.maml_update(clone, adapt_lr, gradients)


def meta_surrogate_loss(iteration_replays, iteration_policies, policy, baseline, tau, gamma, adapt_lr):
    mean_loss = 0.0
    mean_kl = 0.0
    for task_replays, old_policy in tqdm(zip(iteration_replays, iteration_policies),
                                         total=len(iteration_replays),
                                         desc='Surrogate Loss',
                                         leave=False):
        policy.reset_context()
        train_replays = task_replays[:-1]
        valid_episodes = task_replays[-1]
        new_policy = l2l.clone_module(policy)

        # Fast Adapt
        for train_episodes in train_replays:
            new_policy = fast_adapt_a2c(new_policy, train_episodes, adapt_lr,
                                        baseline, gamma, tau, first_order=False)

        # Useful values
        states = valid_episodes.state()
        actions = valid_episodes.action()
        next_states = valid_episodes.next_state()
        rewards = valid_episodes.reward()
        dones = valid_episodes.done()

        # Compute KL
        old_densities = old_policy.density(states)
        new_densities = new_policy.density(states)
        kl = kl_divergence(new_densities, old_densities).mean()
        mean_kl += kl

        # Compute Surrogate Loss
        advantages = compute_advantages(baseline, tau, gamma, rewards, dones, states, next_states)
        advantages = ch.normalize(advantages).detach()
        old_log_probs = old_densities.log_prob(actions).mean(dim=1, keepdim=True).detach()
        new_log_probs = new_densities.log_prob(actions).mean(dim=1, keepdim=True)
        mean_loss += trpo.policy_loss(new_log_probs, old_log_probs, advantages)
    mean_kl /= len(iteration_replays)
    mean_loss /= len(iteration_replays)
    return mean_loss, mean_kl


def main(
        env_name='Particles2D-v1',
        adapt_lr=0.1,
        meta_lr=1.0,
        adapt_steps=1,
        num_iterations=1000,
        meta_bsz=20,
        adapt_bsz=20,
        tau=1.00,
        gamma=0.95,
        seed=42,
        num_workers=10,
        cuda=0,
        num_context_params=2
):
    cuda = bool(cuda)
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    device_name = 'cpu'
    if cuda:
        torch.cuda.manual_seed(seed)
        device_name = 'cuda'
    device = torch.device(device_name)

    def make_env():
        env = gym.make(env_name)
        env = ch.wrappers.ActionSpaceScaler(env)
        return env

    env = l2l.gym.AsyncVectorEnv([make_env for _ in range(num_workers)])
    # env.seed(seed)
    env.set_task(env.sample_tasks(1)[0])
    env = ch.wrappers.Torch(env)
    policy = CaviaDiagNormalPolicy(env.state_size, env.action_size, num_context_params=num_context_params, device=device)
    baseline = LinearValue(env.state_size, env.action_size)

    for iteration in range(num_iterations):
        iteration_reward = 0.0
        iteration_replays = []
        iteration_policies = []

        for task_config in tqdm(env.sample_tasks(meta_bsz), leave=False, desc='Data'):  # Samples a new config
            # deepcopy is not working here
            clone = l2l.clone_module(policy)

            env.set_task(task_config)
            env.reset()
            policy.reset_context()
            task = ch.wrappers.Runner(env)
            task_replay = []

            # Fast Adapt
            for step in range(adapt_steps):
                train_episodes = task.run(clone, episodes=adapt_bsz)
                if cuda:
                    train_episodes = train_episodes.to(device, non_blocking=True)
                clone = fast_adapt_a2c(clone, train_episodes, adapt_lr,
                                       baseline, gamma, tau, first_order=True)
                task_replay.append(train_episodes)

            # Compute Validation Loss
            valid_episodes = task.run(clone, episodes=adapt_bsz)
            task_replay.append(valid_episodes)
            iteration_reward += valid_episodes.reward().sum().item() / adapt_bsz
            iteration_replays.append(task_replay)
            iteration_policies.append(clone)

        # Print statistics
        print('\nIteration', iteration)
        adaptation_reward = iteration_reward / meta_bsz
        print('adaptation_reward', adaptation_reward)

        # TRPO meta-optimization
        backtrack_factor = 0.8
        ls_max_steps = 15
        max_kl = 0.01
        if cuda:
            baseline = baseline.to(device, non_blocking=True)
            iteration_replays = [[r.to(device, non_blocking=True) for r in task_replays] for task_replays in
                                 iteration_replays]

        # Compute CG step direction
        old_loss, old_kl = meta_surrogate_loss(iteration_replays, iteration_policies, policy, baseline, tau, gamma,
                                               adapt_lr)
        grad = autograd.grad(old_loss,
                             policy.parameters(),
                             retain_graph=True)
        grad = parameters_to_vector([g.detach() for g in grad])
        Fvp = trpo.hessian_vector_product(old_kl, policy.parameters())
        step = trpo.conjugate_gradient(Fvp, grad)
        shs = 0.5 * torch.dot(step, Fvp(step))
        lagrange_multiplier = torch.sqrt(shs / max_kl)
        step = step / lagrange_multiplier
        step_ = [torch.zeros_like(p.data) for p in policy.parameters()]
        vector_to_parameters(step, step_)
        step = step_
        del old_kl, Fvp, grad
        old_loss.detach_()

        # Line-search
        for ls_step in range(ls_max_steps):
            stepsize = backtrack_factor ** ls_step * meta_lr
            clone = l2l.clone_module(policy)

            for p, u in zip(clone.parameters(), step):
                p.data.add_(-stepsize, u.data)
            new_loss, kl = meta_surrogate_loss(iteration_replays, iteration_policies, clone, baseline, tau, gamma,
                                               adapt_lr)
            if new_loss < old_loss and kl < max_kl:
                for p, u in zip(policy.parameters(), step):
                    p.data.add_(-stepsize, u.data)
                break


if __name__ == '__main__':
    main()