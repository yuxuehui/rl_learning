from stable_baselines3 import HerReplayBuffer, SAC,PPO
from sb3_contrib import ARS, QRDQN, TQC, TRPO, RecurrentPPO
import gymnasium
import numpy as np
from typing import Any, ClassVar, Dict, Iterable, List, Optional, Tuple, Type, TypeVar, Union
from stable_baselines3.common.noise import ActionNoise, VectorizedActionNoise
from gymnasium import spaces
from stable_baselines3.common.vec_env import (
    DummyVecEnv,
    unwrap_vec_normalize,
)
from stable_baselines3.common.buffers import DictReplayBuffer
from stable_baselines3.common.evaluation import evaluate_policy

from model import SACEnvSwitchWrapper
from utils import make_env,init_env,save_to_csv,get_state,states_to_result,states_to_string
import argparse

import numpy
import time
# import gym
import datetime

init_env()
from video import VideoRecorder

import csv

def train(args):
    env_id = args.domain_name
    cur_time = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S-%f")
    # log_dir = './panda_push_v3_tensorboard/'
    log_dir = './' + args.domain_name + '_tensorboard/'
    

    from envs.skill_choose import TestEnv
    env_1 = TestEnv(info_phase_length=10, name=env_id, lateral_friction=args.test_lateral_friction, 
                    spinning_friction=args.test_spinning_friction, mass=args.test_mass, gravity=args.test_gravity, object_height=args.test_object_height,
                    time_steps=args.time_step//4,reward_type='Dense')
    max_ep_len = 10
    env_targets = [10] # 需要再看看，最大的return大约是多少
    scale = 1
    train_env = env_1
    
    # SAC train model
    # model = PPO("MlpPolicy", env = train_env,
    #                         policy_kwargs=dict(
    #                             net_arch=[512, 512, 512],
    #                             n_critics=2,),
    #                             verbose=1,
    #                             tensorboard_log=log_dir)
    model = SACEnvSwitchWrapper(policy = "MlpPolicy",
                            env = train_env,
                            batch_size=2048,
                            gamma=0.95,
                            learning_rate=1e-4,
                            train_freq=64,
                            gradient_steps=64,
                            tau=0.05,
                            # replay_buffer_class=DictReplayBuffer,
                            # replay_buffer_kwargs=dict(
                            #     n_sampled_goal=4,
                            #     goal_selection_strategy="future",
                            # ),
                            policy_kwargs=dict(
                                net_arch=[512, 512, 512],
                                n_critics=2,
                            ),
                            learning_starts = 1000,
                            verbose=1,
                            tensorboard_log=log_dir)

    model.learn(total_timesteps=args.time_step,progress_bar=True,
                tb_log_name=f"SAC-mass{args.test_mass}-friction{args.test_lateral_friction}-{args.test_gravity}-{args.test_object_height}")
    model.save(f'checkpoints/SAC-{args.domain_name}-mass{args.test_mass}-friction{args.test_lateral_friction}-gravity{-args.test_gravity}-object_height{args.test_object_height}-{cur_time}')
    
    train_env.close()

def generate_video(args):

    env = make_env(args.domain_name, args.test_lateral_friction, args.test_spinning_friction,
                    args.test_mass, args.test_gravity, args.test_object_height)
    test_env = DummyVecEnv([env])

    recoder = VideoRecorder('./video')
    
    #test_env = RecordVideo(test_env, './video')
    observations = test_env.reset()
    states = None
    episode_starts = np.ones((test_env.num_envs,), dtype=bool)
    
    model = SACEnvSwitchWrapper.load(args.test_model_path,env=test_env)
    recoder.record(test_env)
    while True:
        
        # test_env.render(mode='human')
        
        actions, states = model.predict(
            observations,  # type: ignore[arg-type]
            state=states,
            episode_start=episode_starts,
            deterministic=True,
        )
        observations, rewards, dones, infos = test_env.step(actions)
        recoder.record(test_env)
        object = test_env.envs[0].unwrapped.sim._bodies_idx['object']
        table = test_env.envs[0].unwrapped.sim._bodies_idx['table']
        robot = test_env.envs[0].unwrapped.sim._bodies_idx['panda']
        contact_points1 = test_env.envs[0].unwrapped.sim.physics_client.getContactPoints(bodyA = robot,bodyB = object, linkIndexA = 9, linkIndexB = -1)
        contact_points2 = test_env.envs[0].unwrapped.sim.physics_client.getContactPoints(bodyA = robot,bodyB = object, linkIndexA = 10, linkIndexB = -1)

        contact_points = test_env.envs[0].unwrapped.sim.physics_client.getContactPoints(bodyA=table, bodyB=object, linkIndexA=-1,linkIndexB = -1)
        # print("object position: ", test_env.envs[0].unwrapped.sim.physics_client.getBasePositionAndOrientation(bodyUniqueId=object)[0])
        # print('contact num between table and object: ',len(contact_points))
        # print('contact distance between table and object: ',test_env.envs[0].unwrapped.robot.get_fingers_width())
        # print('contact num between table and fingers: ', int(len(contact_points1) > 0) + int(len(contact_points2) > 0))
        # # print(contact_points1)
        # # print(contact_points2)
        # print(infos)
        print(get_state(test_env,args))
        if dones:
            break
    
    cur_time = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S-%f")
    recoder.save(f'train-{args.test_model_path.split("/")[-1]}-test-{args.domain_name}-mass{args.test_mass}-friction{args.test_lateral_friction}-gravity{-args.test_gravity}-object_height{args.test_object_height}-{cur_time}.mp4')
    test_env.close()

def test_success_rate_and_done_type(args):
    env = make_env(args.domain_name, args.test_lateral_friction, args.test_spinning_friction,
                    args.test_mass, args.test_gravity, args.test_object_height)
    test_env = DummyVecEnv([env])
    model = SACEnvSwitchWrapper.load(args.test_model_path,env=test_env)
    cur_time = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S-%f")
    recoder = None
    if args.save_video:
        train_name = f'train-{args.test_model_path.split("/")[-1]}'
        test_name = f'test-{args.domain_name}-mass{args.test_mass}-friction{args.test_lateral_friction}-gravity{-args.test_gravity}-object_height{args.test_object_height}'
        recoder = VideoRecorder(f'./video/{train_name}/{test_name}')

    all_count = 0
    success_count = 0
    pick_and_place_count = 0
    roll_count = 0
    push_count = 0
    
    eps_states = []
    eps_set = set()
    while len(eps_states) < 100:
        #test_env = RecordVideo(test_env, './video')
        observations = test_env.reset()
        if recoder is not None: recoder.reset()
        states = None
        episode_starts = np.ones((test_env.num_envs,), dtype=bool)
        _eps_states = []
        for eps_i in range(50):
            
            actions, states = model.predict(
                observations,  # type: ignore[arg-type]
                state=states,
                episode_start=episode_starts,
                deterministic=True,
            )
            if recoder is not None: recoder.record(test_env)
            observations, rewards, dones, infos = test_env.step(actions)
            if not dones:
                _eps_states.append(get_state(test_env,args) + f"_{actions[0][-1]:.2f}")

            # 一上来就完成
            if dones and eps_i <= 5:
                break

            elif dones:
                if infos[0]['is_success']:
                    success_count += 1
                    _eps_states.append('success')
                else:
                    _eps_states.append('fail')
                all_count += 1
                break
        
        # 一上来就成功不纳入计算
        if len(_eps_states)==0 or (_eps_states[-1] !='success' and _eps_states[-1] !='fail'):
            continue
        
        string = states_to_string(_eps_states)
        result = states_to_result(_eps_states)
        if result == 'pickandplace':
            pick_and_place_count += 1
        elif result == 'roll':
            roll_count += 1
        else:
            push_count += 1

        if recoder is not None and string not in eps_set:
            eps_set.add(string)
            recoder.save(f'{string}-{cur_time}.mp4')
        eps_states.append(_eps_states)
    
    # # 生成视频
    # for _ in range(10):
    #     generate_video(args)

    csv_file_name = f'csv/train-{args.test_model_path.split("/")[-1]}-test-{args.domain_name}-mass{args.test_mass}-friction{args.test_lateral_friction}-gravity{-args.test_gravity}-object_height{args.test_object_height}-{cur_time}.csv'
    save_to_csv(eps_states, csv_file_name)
    print(args.__dict__)
    print('success_rate:', success_count / all_count)
    print('pick_and_place_rate:', pick_and_place_count / all_count)
    print('roll_rate:', roll_count / all_count)
    print('push_rate:', push_count / all_count)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--domain_name', default='PandaPush-v3')
    parser.add_argument('--random_int', default=[1, 5], nargs='+', type=int)
    parser.add_argument('--random_float', default=[0.001, 0.01], nargs='+', type=float)
    parser.add_argument('--test_mass', default=1.0, type=float)
    parser.add_argument('--time_step', default=2000000, type=int)
    parser.add_argument('--test_spinning_friction', default=0.001, type=float)
    parser.add_argument('--test_lateral_friction', default=1.0, type=float)
    parser.add_argument('--test_gravity', default=-9.81, type=float)
    parser.add_argument('--test_object_height', default=1.0, type=float)

    parser.add_argument('--test_model_path', default='SAC-mass1.0-friction20.0', type=str)
    parser.add_argument('--test_mode',action="store_true", default=False)
    parser.add_argument('--test_rate_mode',action="store_true", default=False)
    parser.add_argument('--save_video',action="store_true", default=False)

    args = parser.parse_args()
    
    if not args.test_mode and not args.test_rate_mode:
        train(args)
    elif args.test_mode:
        generate_video(args)
    else:
        test_success_rate_and_done_type(args)
