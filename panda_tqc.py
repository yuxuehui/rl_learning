from stable_baselines3 import HerReplayBuffer, SAC
from sb3_contrib import ARS, QRDQN, TQC, TRPO, RecurrentPPO
import gymnasium
import panda_gym
import numpy as np
from typing import Any, ClassVar, Dict, Iterable, List, Optional, Tuple, Type, TypeVar, Union
from stable_baselines3.common.noise import ActionNoise, VectorizedActionNoise
from gymnasium import spaces
from stable_baselines3.common.vec_env import (
    DummyVecEnv,
    unwrap_vec_normalize,
)
from stable_baselines3.common.evaluation import evaluate_policy

from model import TQCEnvSwitchWrapper
from utils import make_env
import argparse

import numpy


def train(args):
    env_id = args.domain_name
    # log_dir = './panda_push_v3_tensorboard/'
    log_dir = './' + args.domain_name + '_tensorboard/'

    env = make_env(env_id, args.test_lateral_friction, args.test_spinning_friction, args.test_mass)
    train_env = DummyVecEnv([env,env,env,env])
    
    # SAC train model
    model = TQCEnvSwitchWrapper(policy = "MultiInputPolicy",
                            env = train_env,
                            batch_size=2048,
                            gamma=0.95,
                            learning_rate=1e-4,
                            train_freq=64,
                            gradient_steps=64,
                            tau=0.05,
                            replay_buffer_class=HerReplayBuffer,
                            replay_buffer_kwargs=dict(
                                n_sampled_goal=4,
                                goal_selection_strategy="future",
                            ),
                            policy_kwargs=dict(
                                net_arch=[512, 512, 512],
                                n_critics=2,
                            ),
                            learning_starts = 1000,
                            verbose=1,
                            tensorboard_log=log_dir)

    model.learn(total_timesteps=args.time_step,progress_bar=True,tb_log_name=f"TQC-mass{args.test_mass}-friction{args.test_lateral_friction}")
    model.save(f'TQC-mass{args.test_mass}-friction{args.test_lateral_friction}')
    train_env.close()


def test(args):
    # env for train
    env1 = make_env(args.domain_name)
    env2 = make_env(args.domain_name, 1.0, 0.001,2.0)
    env3 = make_env(args.domain_name, 1.0, 0.001,3.0)
    env4 = make_env(args.domain_name, 1.0, 0.001,4.0)
    # env for test
    env5 = make_env(args.domain_name, 1.0, 0.001,10)

    train_env = DummyVecEnv([env1,env2,env3,env4])
    test_env = DummyVecEnv([env5,env5,env5,env5])

    model = TQCEnvSwitchWrapper.load('TQC-PandaPush-v3',env=train_env)
    # model.env = train_env
    # train_mean_reward, train_std_reward = evaluate_policy(model, train_env, 100)
    test_mean_reward, test_std_reward = evaluate_policy(model, test_env, 100)
    
    # print(f"Train Mean reward = {train_mean_reward:.2f} +/- {train_std_reward:.2f}")
    print(f"Test Mean reward = {test_mean_reward:.2f} +/- {test_std_reward:.2f}")

    train_env.close()
    test_env.close()


def retrain(args):
    # env for test
    env5 = make_env(args.domain_name, 1.0, 0.001,50)
    test_env = DummyVecEnv([env5,env5,env5,env5])

    model = TQCEnvSwitchWrapper.load('TQC-PandaPush-v3',env=test_env)
    model.eval_env = True

    model.learn(total_timesteps=args.time_step,progress_bar=True)

    test_env.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--domain_name', default='PandaPush-v3')
    parser.add_argument('--random_int', default=[1, 5], nargs='+', type=int)
    parser.add_argument('--random_float', default=[0.001, 0.01], nargs='+', type=float)
    parser.add_argument('--test_mass', default=1.0, type=int)
    parser.add_argument('--time_step', default=800000, type=int)
    parser.add_argument('--test_spinning_friction', default=0.001, type=float)
    parser.add_argument('--test_lateral_friction', default=1.0, type=float)
    args = parser.parse_args()

    train(args)