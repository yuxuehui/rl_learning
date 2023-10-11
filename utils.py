
import panda_gym
import gymnasium


def get_push_env(lateral_friction=1.0,spinning_friction=0.001,mass=1.0):
    def _init():
        env = gymnasium.make('PandaPickAndPlace-v3')
        # env.unwrapped.sim.set_lateral_friction('object', -1, lateral_friction=lateral_friction)
        # env.unwrapped.sim.set_spinning_friction('object', -1, spinning_friction=spinning_friction)
        
        env.unwrapped.task.goal_range_high[-1] = 0
        block_uid = env.unwrapped.sim._bodies_idx['object']
        env.unwrapped.sim.physics_client.changeDynamics(bodyUniqueId=block_uid, linkIndex=-1, mass=mass)
        # wrapped_env = gym.wrappers.RecordEpisodeStatistics(env, 50)  # Records episode-reward
        # change table's friction
        env.unwrapped.sim.set_lateral_friction('table', -1, lateral_friction=lateral_friction)
        env.unwrapped.sim.set_spinning_friction('table', -1, spinning_friction=spinning_friction)
        block_uid = env.unwrapped.sim._bodies_idx['object']
        print("Info of objects", env.unwrapped.sim.physics_client.getDynamicsInfo(bodyUniqueId=block_uid, linkIndex=-1))
        block_uid = env.unwrapped.sim._bodies_idx['table']
        print("Info of Table", env.unwrapped.sim.physics_client.getDynamicsInfo(bodyUniqueId=block_uid, linkIndex=-1))
        env.reset()
        return env
    return _init

def get_push_dense_env(lateral_friction=1.0,spinning_friction=0.001,mass=1.0):
    def _init():
        env = gymnasium.make('PandaPickAndPlaceDense-v3')
        # env.unwrapped.sim.set_lateral_friction('object', -1, lateral_friction=lateral_friction)
        # env.unwrapped.sim.set_spinning_friction('object', -1, spinning_friction=spinning_friction)

        env.unwrapped.task.goal_range_high[-1] = 0
        # env.unwrapped.sim.set_lateral_friction('object', -1, lateral_friction=lateral_friction)
        # env.unwrapped.sim.set_spinning_friction('object', -1, spinning_friction=spinning_friction)
        block_uid = env.unwrapped.sim._bodies_idx['object']
        env.unwrapped.sim.physics_client.changeDynamics(bodyUniqueId=block_uid, linkIndex=-1, mass=mass)
        # wrapped_env = gym.wrappers.RecordEpisodeStatistics(env, 50)  # Records episode-reward
        # change table's friction
        env.unwrapped.sim.set_lateral_friction('table', -1, lateral_friction=lateral_friction)
        env.unwrapped.sim.set_spinning_friction('table', -1, spinning_friction=spinning_friction)
        block_uid = env.unwrapped.sim._bodies_idx['object']
        print("Info of objects", env.unwrapped.sim.physics_client.getDynamicsInfo(bodyUniqueId=block_uid, linkIndex=-1))
        block_uid = env.unwrapped.sim._bodies_idx['table']
        print("Info of Table", env.unwrapped.sim.physics_client.getDynamicsInfo(bodyUniqueId=block_uid, linkIndex=-1))
        env.reset()
        return env
    return _init

def get_push_joints_env(lateral_friction=1.0,spinning_friction=0.001,mass=1.0):
    def _init():
        env = gymnasium.make('PandaPushJoints-v3')
        env.unwrapped.sim.set_lateral_friction('object', -1, lateral_friction=lateral_friction)
        env.unwrapped.sim.set_spinning_friction('object', -1, spinning_friction=spinning_friction)
        block_uid = env.unwrapped.sim._bodies_idx['object']
        env.unwrapped.sim.physics_client.changeDynamics(bodyUniqueId=block_uid, linkIndex=-1, mass=mass)
        # change table's friction
        env.unwrapped.sim.set_lateral_friction('table', -1, lateral_friction=lateral_friction)
        env.unwrapped.sim.set_spinning_friction('table', -1, spinning_friction=spinning_friction)
        block_uid = env.unwrapped.sim._bodies_idx['object']
        print("Info of objects", env.unwrapped.sim.physics_client.getDynamicsInfo(bodyUniqueId=block_uid, linkIndex=-1))
        block_uid = env.unwrapped.sim._bodies_idx['table']
        print("Info of Table", env.unwrapped.sim.physics_client.getDynamicsInfo(bodyUniqueId=block_uid, linkIndex=-1))
        return env
    return _init

def get_push_joints_dense_env(lateral_friction=1.0,spinning_friction=0.001,mass=1.0):
    def _init():
        env = gymnasium.make('PandaPushJointsDense-v3')
        env.unwrapped.sim.set_lateral_friction('object', -1, lateral_friction=lateral_friction)
        env.unwrapped.sim.set_spinning_friction('object', -1, spinning_friction=spinning_friction)
        block_uid = env.unwrapped.sim._bodies_idx['object']
        env.unwrapped.sim.physics_client.changeDynamics(bodyUniqueId=block_uid, linkIndex=-1, mass=mass)
        # change table's friction
        env.unwrapped.sim.set_lateral_friction('table', -1, lateral_friction=lateral_friction)
        env.unwrapped.sim.set_spinning_friction('table', -1, spinning_friction=spinning_friction)
        block_uid = env.unwrapped.sim._bodies_idx['object']
        print("Info of objects", env.unwrapped.sim.physics_client.getDynamicsInfo(bodyUniqueId=block_uid, linkIndex=-1))
        block_uid = env.unwrapped.sim._bodies_idx['table']
        print("Info of Table", env.unwrapped.sim.physics_client.getDynamicsInfo(bodyUniqueId=block_uid, linkIndex=-1))
        return env
    return _init


def get_pick_and_place_env(lateral_friction=1.0,spinning_friction=0.001,mass=1.0):
    def _init():
        env = gymnasium.make('PandaPickAndPlace-v3')
        # env.unwrapped.sim.set_lateral_friction('object', -1, lateral_friction=lateral_friction)
        # env.unwrapped.sim.set_spinning_friction('object', -1, spinning_friction=spinning_friction)
        block_uid = env.unwrapped.sim._bodies_idx['object']
        env.unwrapped.sim.physics_client.changeDynamics(bodyUniqueId=block_uid, linkIndex=-1, mass=mass)
        # change table's friction
        env.unwrapped.sim.set_lateral_friction('table', -1, lateral_friction=lateral_friction)
        env.unwrapped.sim.set_spinning_friction('table', -1, spinning_friction=spinning_friction)
        block_uid = env.unwrapped.sim._bodies_idx['object']
        print("Info of objects", env.unwrapped.sim.physics_client.getDynamicsInfo(bodyUniqueId=block_uid, linkIndex=-1))
        block_uid = env.unwrapped.sim._bodies_idx['table']
        print("Info of Table", env.unwrapped.sim.physics_client.getDynamicsInfo(bodyUniqueId=block_uid, linkIndex=-1))
        env.reset()
        return env
    return _init
    
def get_pick_and_place_dense_env(lateral_friction=1.0,spinning_friction=0.001,mass=1.0):
    def _init():
        env = gymnasium.make('PandaPickAndPlaceDense-v3')
        # env.unwrapped.sim.set_lateral_friction('object', -1, lateral_friction=lateral_friction)
        # env.unwrapped.sim.set_spinning_friction('object', -1, spinning_friction=spinning_friction)
        block_uid = env.unwrapped.sim._bodies_idx['object']
        env.unwrapped.sim.physics_client.changeDynamics(bodyUniqueId=block_uid, linkIndex=-1, mass=mass)
        # change table's friction
        env.unwrapped.sim.set_lateral_friction('table', -1, lateral_friction=lateral_friction)
        env.unwrapped.sim.set_spinning_friction('table', -1, spinning_friction=spinning_friction)
        block_uid = env.unwrapped.sim._bodies_idx['object']
        print("Info of objects", env.unwrapped.sim.physics_client.getDynamicsInfo(bodyUniqueId=block_uid, linkIndex=-1))
        block_uid = env.unwrapped.sim._bodies_idx['table']
        print("Info of Table", env.unwrapped.sim.physics_client.getDynamicsInfo(bodyUniqueId=block_uid, linkIndex=-1))
        env.reset()
        return env
    return _init

def get_reach_env(lateral_friction=1.0,spinning_friction=0.001,mass=1.0):
    # NO OBJECT!!!!!!!
    def _init():
        env = gymnasium.make('PandaReach-v3')
        # print(env.unwrapped.sim._bodies_idx.keys())
        # dict_keys(['panda', 'plane', 'table', 'target'])
        # env.unwrapped.sim.set_lateral_friction('object', -1, lateral_friction=lateral_friction)
        # env.unwrapped.sim.set_spinning_friction('object', -1, spinning_friction=spinning_friction)
        block_uid = env.unwrapped.sim._bodies_idx['object']
        env.unwrapped.sim.physics_client.changeDynamics(bodyUniqueId=block_uid, linkIndex=-1, mass=mass)
        return env
    return _init

def get_slide_env(lateral_friction=1.0,spinning_friction=0.001,mass=1.0):
    def _init():
        env = gymnasium.make('PandaSlide-v3')
        env.unwrapped.sim.set_lateral_friction('object', -1, lateral_friction=lateral_friction)
        env.unwrapped.sim.set_spinning_friction('object', -1, spinning_friction=spinning_friction)
        block_uid = env.unwrapped.sim._bodies_idx['object']
        env.unwrapped.sim.physics_client.changeDynamics(bodyUniqueId=block_uid, linkIndex=-1, mass=mass)
        # change table's friction
        env.unwrapped.sim.set_lateral_friction('table', -1, lateral_friction=lateral_friction)
        env.unwrapped.sim.set_spinning_friction('table', -1, spinning_friction=spinning_friction)
        block_uid = env.unwrapped.sim._bodies_idx['object']
        print("Info of objects", env.unwrapped.sim.physics_client.getDynamicsInfo(bodyUniqueId=block_uid, linkIndex=-1))
        block_uid = env.unwrapped.sim._bodies_idx['table']
        print("Info of Table", env.unwrapped.sim.physics_client.getDynamicsInfo(bodyUniqueId=block_uid, linkIndex=-1))
        return env
    return _init

def get_stack_env(lateral_friction=1.0,spinning_friction=0.001,mass=1.0):
    def _init():
        env = gymnasium.make('PandaStack-v3')
        env.unwrapped.sim.set_lateral_friction('object1', -1, lateral_friction=lateral_friction)
        env.unwrapped.sim.set_spinning_friction('object1', -1, spinning_friction=spinning_friction)
        env.unwrapped.sim.set_lateral_friction('object2', -1, lateral_friction=lateral_friction)
        env.unwrapped.sim.set_spinning_friction('object2', -1, spinning_friction=spinning_friction)
        block_uid1 = env.unwrapped.sim._bodies_idx['object1']
        env.unwrapped.sim.physics_client.changeDynamics(bodyUniqueId=block_uid1, linkIndex=-1, mass=mass)
        block_uid2 = env.unwrapped.sim._bodies_idx['object2']
        env.unwrapped.sim.physics_client.changeDynamics(bodyUniqueId=block_uid2, linkIndex=-1, mass=mass)
        # change table's friction
        env.unwrapped.sim.set_lateral_friction('table', -1, lateral_friction=lateral_friction)
        env.unwrapped.sim.set_spinning_friction('table', -1, spinning_friction=spinning_friction)
        block_uid = env.unwrapped.sim._bodies_idx['object1']
        print("Info of objects", env.unwrapped.sim.physics_client.getDynamicsInfo(bodyUniqueId=block_uid, linkIndex=-1))
        block_uid = env.unwrapped.sim._bodies_idx['table']
        print("Info of Table", env.unwrapped.sim.physics_client.getDynamicsInfo(bodyUniqueId=block_uid, linkIndex=-1))
        return env
    return _init



def make_env(name,lateral_friction=1.0,spinning_friction=0.001,mass=1.0):
    print(name)
    if name == "PandaPush-v3":
        print("This is PandaPush-v3 Env, Welcome!")
        return get_push_env(lateral_friction, spinning_friction, mass)
    elif name == "PandaPickAndPlace-v3":
        print("This is PandaPickAndPlace-v3 Env, Welcome!")
        return get_pick_and_place_env(lateral_friction, spinning_friction, mass)
    elif name == "PandaPushDense-v3":
        print("This is PandaPushDense-v3 Env, Welcome!")
        return get_push_dense_env(lateral_friction, spinning_friction, mass)
    elif name == "PandaPickAndPlaceDense-v3":
        print("This is PandaPushDense-v3 Env, Welcome!")
        return get_pick_and_place_dense_env(lateral_friction, spinning_friction, mass)
    elif name == "PandaPushJoints-v3":
        print("This is PandaPushJoints-v3 Env, Welcome!")
        return get_push_joints_env(lateral_friction, spinning_friction, mass)
    elif name == "PandaPushJointsDense-v3":
        print("This is PandaPushJointsDense-v3 Env, Welcome!")
        return get_push_joints_dense_env(lateral_friction, spinning_friction, mass)
    elif name == "PandaReach-v3":
        print("This is PandaReach-v3 Env, Welcome!")
        return get_reach_env(lateral_friction, spinning_friction, mass)
    elif name == "PandaSlide-v3":
        print("This is PandaSlide-v3 Env, Welcome!")
        return get_slide_env(lateral_friction, spinning_friction, mass)
    elif name == "PandaStack-v3":
        print("This is PandaStack-v3 Env, Welcome!")
        return get_stack_env(lateral_friction, spinning_friction, mass)
    else:
        print("Unkown Environment!! ")
    
