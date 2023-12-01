

echo "test_mass 0.5"
python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 0.5 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass1.0-friction1.0-gravity9.81-object_height1.0-2023-11-22-22:10:05-167151 --test_rate_mode

echo "test_mass 1.0"
python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 1.0 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass1.0-friction1.0-gravity9.81-object_height1.0-2023-11-22-22:10:05-167151 --test_rate_mode

echo "test_mass 1.5"
python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 1.5 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass1.0-friction1.0-gravity9.81-object_height1.0-2023-11-22-22:10:05-167151 --test_rate_mode

echo "test_mass 2.0"
python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 2.0 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass1.0-friction1.0-gravity9.81-object_height1.0-2023-11-22-22:10:05-167151 --test_rate_mode

echo "test_mass 10"
python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 10 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass1.0-friction1.0-gravity9.81-object_height1.0-2023-11-22-22:10:05-167151 --test_rate_mode


echo "test_mass 1"
python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 1 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass1.0-friction1.0-gravity9.81-object_height1.0-2023-11-22-22:12:07-749569 --test_rate_mode

echo "test_mass 2"
python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 2 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass1.0-friction1.0-gravity9.81-object_height1.0-2023-11-22-22:12:07-749569 --test_rate_mode

echo "test_mass 3"
python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 3 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass1.0-friction1.0-gravity9.81-object_height1.0-2023-11-22-22:12:07-749569 --test_rate_mode

echo "test_mass 4"
python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 4 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass1.0-friction1.0-gravity9.81-object_height1.0-2023-11-22-22:12:07-749569 --test_rate_mode

echo "test_mass 10"
python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 10 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass1.0-friction1.0-gravity9.81-object_height1.0-2023-11-22-22:12:07-749569 --test_rate_mode

