

echo "test_lateral_friction 0.1"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 0.1 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction1.0-gravity9.81-object_height1.0-2023-11-22-22:22:44-137235 --test_rate_mode

echo "test_lateral_friction 0.2"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 0.2 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction1.0-gravity9.81-object_height1.0-2023-11-22-22:22:44-137235 --test_rate_mode

echo "test_lateral_friction 0.5"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 0.5 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction1.0-gravity9.81-object_height1.0-2023-11-22-22:22:44-137235 --test_rate_mode

echo "test_lateral_friction 1.0"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 1.0 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction1.0-gravity9.81-object_height1.0-2023-11-22-22:22:44-137235 --test_rate_mode

echo "test_lateral_friction 10"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 10 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction1.0-gravity9.81-object_height1.0-2023-11-22-22:22:44-137235 --test_rate_mode


echo "test_lateral_friction 1"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 1 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction1.0-gravity9.81-object_height1.0-2023-11-22-22:23:33-158279 --test_rate_mode

echo "test_lateral_friction 2"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 2 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction1.0-gravity9.81-object_height1.0-2023-11-22-22:23:33-158279 --test_rate_mode

echo "test_lateral_friction 3"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 3 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction1.0-gravity9.81-object_height1.0-2023-11-22-22:23:33-158279 --test_rate_mode

echo "test_lateral_friction 4"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 4 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction1.0-gravity9.81-object_height1.0-2023-11-22-22:23:33-158279 --test_rate_mode

echo "test_lateral_friction 10"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 10 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction1.0-gravity9.81-object_height1.0-2023-11-22-22:23:33-158279 --test_rate_mode

