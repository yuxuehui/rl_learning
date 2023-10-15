
from typing import Optional

import numpy as np

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


def get_push_env(lateral_friction=1.0,spinning_friction=0.001,mass=1.0,gravity=-9.81, object_height=1, reward_type = '',control_type=''):
    def _init():
        env = gymnasium.make(f'PandaPickAndPlace{control_type}{reward_type}{object_height}-v3')
        
        env.unwrapped.task.goal_range_high[-1] = 0
        block_uid = env.unwrapped.sim._bodies_idx['object']
        env.unwrapped.sim.physics_client.changeDynamics(bodyUniqueId=block_uid, linkIndex=-1, mass=mass)
        # wrapped_env = gym.wrappers.RecordEpisodeStatistics(env, 50)  # Records episode-reward
        # change table's friction
        env.unwrapped.sim.set_lateral_friction('table', -1, lateral_friction=lateral_friction)
        env.unwrapped.sim.set_spinning_friction('table', -1, spinning_friction=spinning_friction)
        # gravity
        env.unwrapped.sim.physics_client.setGravity(0, 0, gravity)

        block_uid = env.unwrapped.sim._bodies_idx['object']
        print("Info of objects", env.unwrapped.sim.physics_client.getDynamicsInfo(bodyUniqueId=block_uid, linkIndex=-1))
        block_uid = env.unwrapped.sim._bodies_idx['table']
        print("Info of Table", env.unwrapped.sim.physics_client.getDynamicsInfo(bodyUniqueId=block_uid, linkIndex=-1))
        env.reset()
        return env
    return _init


def get_pick_and_place_env(lateral_friction=1.0,spinning_friction=0.001,mass=1.0,gravity=-9.81, object_height=1, reward_type = '',control_type=''):
    def _init():
        env = gymnasium.make(f'PandaPickAndPlace{control_type}{reward_type}{object_height}-v3')

        block_uid = env.unwrapped.sim._bodies_idx['object']
        env.unwrapped.sim.physics_client.changeDynamics(bodyUniqueId=block_uid, linkIndex=-1, mass=mass)
        # change table's friction
        env.unwrapped.sim.set_lateral_friction('table', -1, lateral_friction=lateral_friction)
        env.unwrapped.sim.set_spinning_friction('table', -1, spinning_friction=spinning_friction)
        # gravity
        env.unwrapped.sim.physics_client.setGravity(0, 0, gravity)

        block_uid = env.unwrapped.sim._bodies_idx['object']
        print("Info of objects", env.unwrapped.sim.physics_client.getDynamicsInfo(bodyUniqueId=block_uid, linkIndex=-1))
        block_uid = env.unwrapped.sim._bodies_idx['table']
        print("Info of Table", env.unwrapped.sim.physics_client.getDynamicsInfo(bodyUniqueId=block_uid, linkIndex=-1))
        env.reset()
        return env
    return _init

def make_env(name,lateral_friction=1.0,spinning_friction=0.001,mass=1.0,gravity=-9.81, object_height=1, reward_type = '',control_type=''):
    if name == "PandaPush-v3":
        print("This is PandaPush-v3 Env, Welcome!")
        return get_push_env(lateral_friction, spinning_friction, mass, gravity,object_height,reward_type,control_type )
    elif name == "PandaPickAndPlace-v3":
        print("This is PandaPickAndPlace-v3 Env, Welcome!")
        return get_pick_and_place_env(lateral_friction, spinning_friction, mass, gravity,object_height,reward_type,control_type )
    else:
        raise Exception("Unkown Environment in make_env")
    