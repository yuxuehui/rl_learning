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

from model import SACEnvSwitchWrapper
from utils import make_env
import argparse

import numpy
import time
# import gym


from video import VideoRecorder

def train(args):
    env_id = args.domain_name
    # log_dir = './panda_push_v3_tensorboard/'
    log_dir = './' + args.domain_name + '_tensorboard/'

    env = make_env(env_id, args.test_lateral_friction, args.test_spinning_friction, args.test_mass)
    train_env = DummyVecEnv([env,env,env,env])
    
    # SAC train model
    model = SACEnvSwitchWrapper(policy = "MultiInputPolicy",
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

    model.learn(total_timesteps=args.time_step,progress_bar=True,tb_log_name=f"SAC-mass{args.test_mass}-friction{args.test_lateral_friction}")
    model.save(f'checkpoints/SAC-{args.domain_name}-mass{args.test_mass}-friction{args.test_lateral_friction}')
    
    train_env.close()

def test(args):

    env = make_env(args.domain_name, args.test_lateral_friction, args.test_spinning_friction, args.test_mass)
    test_env = DummyVecEnv([env])

    recoder = VideoRecorder('./video')
    
    #test_env = RecordVideo(test_env, './video')
    observations = test_env.reset()
    states = None
    episode_starts = np.ones((test_env.num_envs,), dtype=bool)
    
    model = SACEnvSwitchWrapper.load(args.test_model_path,env=test_env)
    
    while True:
        recoder.record(test_env)
        # test_env.render(mode='human')
        
        actions, states = model.predict(
            observations,  # type: ignore[arg-type]
            state=states,
            episode_start=episode_starts,
            deterministic=True,
        )
        observations, rewards, dones, infos = test_env.step(actions)
        print(infos)
        if dones:
            break
    
    recoder.save(f'train-{args.test_model_path.split("/")[-1]}-test-{args.domain_name}-mass{args.test_mass}-friction{args.test_lateral_friction}.mp4')
    test_env.close()

def test_success_rate(args):

    env = make_env(args.domain_name, args.test_lateral_friction, args.test_spinning_friction, args.test_mass)
    test_env = DummyVecEnv([env])
    model = SACEnvSwitchWrapper.load(args.test_model_path,env=test_env)
    acc_num = 0
    for i in range(100):
        #test_env = RecordVideo(test_env, './video')
        observations = test_env.reset()
        states = None
        episode_starts = np.ones((test_env.num_envs,), dtype=bool)
        while True:
            # test_env.render(mode='human')
            
            actions, states = model.predict(
                observations,  # type: ignore[arg-type]
                state=states,
                episode_start=episode_starts,
                deterministic=True,
            )
            observations, rewards, dones, infos = test_env.step(actions)
            if dones:
                if infos[0]['is_success']: acc_num += 1
                break
    print('acc_rate:',acc_num / 100)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--domain_name', default='PandaPickAndPlace-v3')
    parser.add_argument('--random_int', default=[1, 5], nargs='+', type=int)
    parser.add_argument('--random_float', default=[0.001, 0.01], nargs='+', type=float)
    parser.add_argument('--test_mass', default=1.0, type=int)
    parser.add_argument('--time_step', default=2000000, type=int)
    parser.add_argument('--test_spinning_friction', default=0.001, type=float)
    parser.add_argument('--test_lateral_friction', default=1.0, type=float)
    
    parser.add_argument('--test_model_path', default='SAC-mass1.0-friction20.0', type=str)
    parser.add_argument('--test_mode',action="store_true", default=False)
    parser.add_argument('--test_rate_mode',action="store_true", default=False)
    args = parser.parse_args()
    
    if not args.test_mode and not args.test_rate_mode:
        train(args)
    elif args.test_mode:
        test(args)
    else:
        test_success_rate(args)
