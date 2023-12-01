
echo "friction 1"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 10 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction1.0-gravity9.81-object_height1.0-2023-11-29-23:14:34-039394 --test_rate_mode

echo "friction 2"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 10 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction1.0-gravity9.81-object_height1.0-2023-11-29-23:14:53-844105 --test_rate_mode

echo "friction 3"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 6 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction1.0-gravity9.81-object_height1.0-2023-11-29-23:15:14-543752 --test_rate_mode

echo "friction 4"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 6 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction1.0-gravity9.81-object_height1.0-2023-11-29-23:15:45-081134 --test_rate_mode


echo "mass 1"
python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 10 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass1.0-friction1.0-gravity9.81-object_height1.0-2023-11-29-20:28:30-593902 --test_rate_mode

echo "mass 2"
python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 10 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass1.0-friction1.0-gravity9.81-object_height1.0-2023-11-29-20:29:10-428830 --test_rate_mode

echo "mass 3"
python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 8 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass1.0-friction1.0-gravity9.81-object_height1.0-2023-11-29-20:29:32-526611 --test_rate_mode

echo "mass 4"
python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 8 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass1.0-friction1.0-gravity9.81-object_height1.0-2023-11-29-20:29:54-912621 --test_rate_mode
