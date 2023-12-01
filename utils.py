
from typing import Optional

import numpy as np
import csv

import gymnasium

def init_env():
    import os
    from gymnasium.envs.registration import register
    ENV_IDS = []

    for task in ["Push", "PickAndPlace"]:
        for reward_type in ["sparse", "dense"]:
            for control_type in ["ee", "joints"]:
                for height in [0.2, 0.5, 1.0, 2.0]:
                    reward_suffix = "Dense" if reward_type == "dense" else ""
                    control_suffix = "Joints" if control_type == "joints" else ""
                    env_id = f"Panda{task}{control_suffix}{reward_suffix}{height}-v3"

                    register(
                        id=env_id,
                        entry_point=f"env:Panda{task}Env",
                        kwargs={"reward_type": reward_type, "control_type": control_type, 'object_height':height},
                        max_episode_steps=100 if task == "Stack" else 50,
                    )

                    ENV_IDS.append(env_id)


def get_push_env(lateral_friction=1.0,spinning_friction=0.001,mass=1.0,gravity=-9.81, object_height=1, reward_type = '',control_type='',train_time_steps=0):
    def _init():
        env = gymnasium.make(f'PandaPush{control_type}{reward_type}{object_height}-v3')
        
        env.task.set_total_train_timesteps(train_time_steps)

        # env.unwrapped.task.goal_range_high[-1] = 0
        block_uid = env.unwrapped.sim._bodies_idx['object']
        env.unwrapped.sim.physics_client.changeDynamics(bodyUniqueId=block_uid, linkIndex=-1, mass=mass)
        # wrapped_env = gym.wrappers.RecordEpisodeStatistics(env, 50)  # Records episode-reward
        # change table's friction
        env.unwrapped.sim.set_lateral_friction('table', -1, lateral_friction=lateral_friction)
        env.unwrapped.sim.set_spinning_friction('table', -1, spinning_friction=spinning_friction)
        # gravity
        env.unwrapped.sim.physics_client.setGravity(0, 0, gravity)
        env.set_obs_friction_mass(lateral_friction,mass)

        block_uid = env.unwrapped.sim._bodies_idx['object']
        print("Info of objects", env.unwrapped.sim.physics_client.getDynamicsInfo(bodyUniqueId=block_uid, linkIndex=-1))
        block_uid = env.unwrapped.sim._bodies_idx['table']
        print("Info of Table", env.unwrapped.sim.physics_client.getDynamicsInfo(bodyUniqueId=block_uid, linkIndex=-1))
        env.reset()
        return env
    return _init


def get_pick_and_place_env(lateral_friction=1.0,spinning_friction=0.001,mass=1.0,gravity=-9.81, object_height=1, reward_type = '',control_type='',train_time_steps=0):
    def _init():
        env = gymnasium.make(f'PandaPickAndPlace{control_type}{reward_type}{object_height}-v3')
        env.task.set_total_train_timesteps(train_time_steps)
        block_uid = env.unwrapped.sim._bodies_idx['object']
        env.unwrapped.sim.physics_client.changeDynamics(bodyUniqueId=block_uid, linkIndex=-1, mass=mass)
        # change table's friction
        env.unwrapped.sim.set_lateral_friction('table', -1, lateral_friction=lateral_friction)
        env.unwrapped.sim.set_spinning_friction('table', -1, spinning_friction=spinning_friction)
        # gravity
        env.unwrapped.sim.physics_client.setGravity(0, 0, gravity)
        env.set_obs_friction_mass(lateral_friction,mass)

        block_uid = env.unwrapped.sim._bodies_idx['object']
        print("Info of objects", env.unwrapped.sim.physics_client.getDynamicsInfo(bodyUniqueId=block_uid, linkIndex=-1))
        block_uid = env.unwrapped.sim._bodies_idx['table']
        print("Info of Table", env.unwrapped.sim.physics_client.getDynamicsInfo(bodyUniqueId=block_uid, linkIndex=-1))
        env.reset()
        return env
    return _init

def make_env(name,lateral_friction=1.0,spinning_friction=0.001,mass=1.0,gravity=-9.81, object_height=1.0, reward_type = '',control_type='',train_time_steps=0):
    if name == "PandaPush-v3":
        print("This is PandaPush-v3 Env, Welcome!")
        return get_push_env(lateral_friction, spinning_friction, mass, gravity,object_height,reward_type,control_type,train_time_steps)
    elif name == "PandaPickAndPlace-v3":
        print("This is PandaPickAndPlace-v3 Env, Welcome!")
        return get_pick_and_place_env(lateral_friction, spinning_friction, mass, gravity,object_height,reward_type,control_type,train_time_steps)
    else:
        raise Exception("Unkown Environment in make_env")


def save_to_csv(data, out_file):

    # 打开CSV文件进行写操作
    with open(out_file, 'w', newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        for _data in data:
            writer.writerow(_data)
        

def get_state(envs,args):
    object = envs.envs[0].unwrapped.sim._bodies_idx['object']
    table = envs.envs[0].unwrapped.sim._bodies_idx['table']
    robot = envs.envs[0].unwrapped.sim._bodies_idx['panda']
    contact_points = envs.envs[0].unwrapped.sim.physics_client.getContactPoints(bodyA=table, bodyB=object, linkIndexA=-1,linkIndexB = -1)
    contact_points1 = envs.envs[0].unwrapped.sim.physics_client.getContactPoints(bodyA = robot,bodyB = object, linkIndexA = 9, linkIndexB = -1)
    contact_points2 = envs.envs[0].unwrapped.sim.physics_client.getContactPoints(bodyA = robot,bodyB = object, linkIndexA = 10, linkIndexB = -1)
    object_info = envs.envs[0].unwrapped.sim.physics_client.getBasePositionAndOrientation(bodyUniqueId=object)
    fingers_width = envs.envs[0].unwrapped.robot.get_fingers_width()

    at_high = object_info[0][2] > 0.021 * args.test_object_height
    # clamp_finger = fingers_width > 0.03 and fingers_width < 0.0405
    zero_table_contact = len(contact_points) == 0
    contact_with_two_fingers = (len(contact_points1) > 0 and len(contact_points2)) > 0
    
    if at_high and zero_table_contact and contact_with_two_fingers:
        return 'pickandplace'
    elif at_high:
        return 'roll'
    elif object_info[0][2] > 0.019 and object_info[0][2]<0.21:
        return 'push'
    else:
        return 'down'

def states_to_result(states):
    for state in states:
        if 'pickandplace' in state:
            return 'pickandplace'
    for state in states:
        if 'roll' in state:
            return 'roll'
    return 'push'

def states_to_string(states):
    tran_dict = {
        'roll':'r',
        'pickandplace':'P',
        'push':'p',
        'down':'d',
        'success':'s',
        'fail':'f',
    }
    _states = [tran_dict[s.split('_')[0]] for s in states]
    return ''.join(_states)