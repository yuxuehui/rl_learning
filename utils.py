
from typing import Optional

import numpy as np

from panda_gym.envs.core import RobotTaskEnv
from panda_gym.envs.robots.panda import Panda
from panda_gym.pybullet import PyBullet
import gymnasium

from panda_gym.envs.tasks.pick_and_place import PickAndPlace
from panda_gym.envs.tasks.push import Push


class PushWrapper(Push):
    def __init__(
        self,
        sim,
        reward_type="sparse",
        distance_threshold=0.05,
        goal_xy_range=0.3,
        obj_xy_range=0.3,
        object_height=1.0,
    ) -> None:
        self.object_height = object_height
        super().__init__(sim,reward_type,distance_threshold,goal_xy_range,obj_xy_range)

    def _create_scene(self) -> None:
        self.sim.create_plane(z_offset=-0.4)
        self.sim.create_table(length=1.1, width=0.7, height=0.4, x_offset=-0.3)
        object_size = np.ones(3) * self.object_size / 2
        object_size[2] = object_size[2] * self.object_height
        object_position = np.array([0.0, 0.0, object_size[2]])
        self.sim.create_box(
            body_name="object",
            half_extents=object_size,
            mass=1.0,
            position=object_position,
            rgba_color=np.array([0.1, 0.9, 0.1, 1.0]),
        )
        self.sim.create_box(
            body_name="target",
            half_extents=object_size,
            mass=0.0,
            ghost=True,
            position=object_position,
            rgba_color=np.array([0.1, 0.9, 0.1, 0.3]),
        )

    def _sample_goal(self) -> np.ndarray:
        """Sample a goal."""
        goal = np.array([0.0, 0.0, self.object_size / 2 * self.object_height])  # z offset for the cube center
        noise = self.np_random.uniform(self.goal_range_low, self.goal_range_high)
        if self.np_random.random() < 0.3:
            noise[2] = 0.0
        goal += noise
        return goal

    def _sample_object(self) -> np.ndarray:
        """Randomize start position of object."""
        object_position = np.array([0.0, 0.0, self.object_size / 2 * self.object_height])
        noise = self.np_random.uniform(self.obj_range_low, self.obj_range_high)
        object_position += noise
        return object_position


class PickAndPlaceWrapper(PickAndPlace):
    def __init__(
        self,
        sim: PyBullet,
        reward_type: str = "sparse",
        distance_threshold: float = 0.05,
        goal_xy_range: float = 0.3,
        goal_z_range: float = 0.2,
        obj_xy_range: float = 0.3,
        object_height: float=1.0,
    ) -> None:
        self.object_height = object_height
        super().__init__(sim,reward_type,distance_threshold,goal_xy_range,goal_z_range,obj_xy_range)

    def _create_scene(self) -> None:
        """Create the scene."""
        self.sim.create_plane(z_offset=-0.4)
        self.sim.create_table(length=1.1, width=0.7, height=0.4, x_offset=-0.3)
        object_size = np.ones(3) * self.object_size / 2
        object_size[2] = object_size[2] * self.object_height
        object_position = np.array([0.0, 0.0, object_size[2]])
        self.sim.create_box(
            body_name="object",
            half_extents=object_size,
            mass=1.0,
            position=object_position,
            rgba_color=np.array([0.1, 0.9, 0.1, 1.0]),
        )
        self.sim.create_box(
            body_name="target",
            half_extents=object_size,
            mass=0.0,
            ghost=True,
            position=np.array([0.0, 0.0, 0.05]),
            rgba_color=np.array([0.1, 0.9, 0.1, 0.3]),
        )
    def _sample_goal(self) -> np.ndarray:
        """Sample a goal."""
        goal = np.array([0.0, 0.0, self.object_size / 2 * self.object_height])  # z offset for the cube center
        noise = self.np_random.uniform(self.goal_range_low, self.goal_range_high)
        if self.np_random.random() < 0.3:
            noise[2] = 0.0
        goal += noise
        return goal

    def _sample_object(self) -> np.ndarray:
        """Randomize start position of object."""
        object_position = np.array([0.0, 0.0, self.object_size / 2 * self.object_height])
        noise = self.np_random.uniform(self.obj_range_low, self.obj_range_high)
        object_position += noise
        return object_position

class PandaPushEnv(RobotTaskEnv):
    """Push task wih Panda robot.

    Args:
        render_mode (str, optional): Render mode. Defaults to "rgb_array".
        reward_type (str, optional): "sparse" or "dense". Defaults to "sparse".
        control_type (str, optional): "ee" to control end-effector position or "joints" to control joint values.
            Defaults to "ee".
        renderer (str, optional): Renderer, either "Tiny" or OpenGL". Defaults to "Tiny" if render mode is "human"
            and "OpenGL" if render mode is "rgb_array". Only "OpenGL" is available for human render mode.
        render_width (int, optional): Image width. Defaults to 720.
        render_height (int, optional): Image height. Defaults to 480.
        render_target_position (np.ndarray, optional): Camera targetting this postion, as (x, y, z).
            Defaults to [0., 0., 0.].
        render_distance (float, optional): Distance of the camera. Defaults to 1.4.
        render_yaw (float, optional): Yaw of the camera. Defaults to 45.
        render_pitch (float, optional): Pitch of the camera. Defaults to -30.
        render_roll (int, optional): Rool of the camera. Defaults to 0.
    """

    def __init__(
        self,
        render_mode: str = "rgb_array",
        reward_type: str = "sparse",
        control_type: str = "ee",
        renderer: str = "Tiny",
        render_width: int = 720,
        render_height: int = 480,
        render_target_position: Optional[np.ndarray] = None,
        render_distance: float = 1.4,
        render_yaw: float = 45,
        render_pitch: float = -30,
        render_roll: float = 0,
        object_height: float = 1,
    ) -> None:
        sim = PyBullet(render_mode=render_mode, renderer=renderer)
        robot = Panda(sim, block_gripper=True, base_position=np.array([-0.6, 0.0, 0.0]), control_type=control_type)
        task = PushWrapper(sim, reward_type=reward_type,object_height=object_height)
        super().__init__(
            robot,
            task,
            render_width=render_width,
            render_height=render_height,
            render_target_position=render_target_position,
            render_distance=render_distance,
            render_yaw=render_yaw,
            render_pitch=render_pitch,
            render_roll=render_roll,
        )


class PandaPickAndPlaceEnv(RobotTaskEnv):
    """Pick and Place task wih Panda robot.

    Args:
        render_mode (str, optional): Render mode. Defaults to "rgb_array".
        reward_type (str, optional): "sparse" or "dense". Defaults to "sparse".
        control_type (str, optional): "ee" to control end-effector position or "joints" to control joint values.
            Defaults to "ee".
        renderer (str, optional): Renderer, either "Tiny" or OpenGL". Defaults to "Tiny" if render mode is "human"
            and "OpenGL" if render mode is "rgb_array". Only "OpenGL" is available for human render mode.
        render_width (int, optional): Image width. Defaults to 720.
        render_height (int, optional): Image height. Defaults to 480.
        render_target_position (np.ndarray, optional): Camera targetting this postion, as (x, y, z).
            Defaults to [0., 0., 0.].
        render_distance (float, optional): Distance of the camera. Defaults to 1.4.
        render_yaw (float, optional): Yaw of the camera. Defaults to 45.
        render_pitch (float, optional): Pitch of the camera. Defaults to -30.
        render_roll (int, optional): Rool of the camera. Defaults to 0.
    """

    def __init__(
        self,
        render_mode: str = "rgb_array",
        reward_type: str = "sparse",
        control_type: str = "ee",
        renderer: str = "Tiny",
        render_width: int = 720,
        render_height: int = 480,
        render_target_position: Optional[np.ndarray] = None,
        render_distance: float = 1.4,
        render_yaw: float = 45,
        render_pitch: float = -30,
        render_roll: float = 0,
        object_height: float = 1,
    ) -> None:
        sim = PyBullet(render_mode=render_mode, renderer=renderer)
        robot = Panda(sim, block_gripper=False, base_position=np.array([-0.6, 0.0, 0.0]), control_type=control_type)
        task = PickAndPlaceWrapper(sim, reward_type=reward_type,object_height=object_height)
        super().__init__(
            robot,
            task,
            render_width=render_width,
            render_height=render_height,
            render_target_position=render_target_position,
            render_distance=render_distance,
            render_yaw=render_yaw,
            render_pitch=render_pitch,
            render_roll=render_roll,
        )

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
                        entry_point=f"Panda{task}Env",
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
    