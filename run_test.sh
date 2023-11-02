
# 计算 mass 的指标
echo "mass 1"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 1 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass1.0-friction1.0-gravity9.81-object_height1.0 --test_rate_mode

echo "mass 5"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 5 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass5-friction1.0-gravity9.81-object_height1.0 --test_rate_mode

echo "mass 10"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 10 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass10-friction1.0-gravity9.81-object_height1.0 --test_rate_mode

echo "mass 15"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 15 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass15-friction1.0-gravity9.81-object_height1.0 --test_rate_mode

echo "mass 20"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 20 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass20-friction1.0 --test_rate_mode


# 计算其他对比指标
echo "mass 1 - 5"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 5 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass1.0-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
echo "mass 1 - 10"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 10 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass1.0-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
echo "mass 1 - 15"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 15 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass1.0-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
echo "mass 1 - 20"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 20 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass1.0-friction1.0-gravity9.81-object_height1.0 --test_rate_mode

# 计算其他对比指标
echo "mass 5 - 1"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 1 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass5-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
echo "mass 5 - 10"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 10 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass5-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
echo "mass 5 - 15"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 15 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass5-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
echo "mass 5 - 20"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 20 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass5-friction1.0-gravity9.81-object_height1.0 --test_rate_mode

# 计算其他对比指标
echo "mass 10 - 1"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 1 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass10-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
echo "mass 10 - 5"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 5 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass10-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
echo "mass 10 - 15"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 15 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass10-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
echo "mass 10 - 20"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 20 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass10-friction1.0-gravity9.81-object_height1.0 --test_rate_mode

# 计算其他对比指标
echo "mass 15 - 1"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 1 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass15-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
echo "mass 15 - 5"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 5 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass15-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
echo "mass 15 - 10"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 10 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass15-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
echo "mass 15 - 20"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 20 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass15-friction1.0-gravity9.81-object_height1.0 --test_rate_mode

# 计算其他对比指标
echo "mass 20 - 1"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 1 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass20-friction1.0 --test_rate_mode
echo "mass 20 - 5"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 5 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass20-friction1.0 --test_rate_mode
echo "mass 20 - 10"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 10 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass20-friction1.0 --test_rate_mode
echo "mass 20 - 15"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 15 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass20-friction1.0 --test_rate_mode

# 计算其他对比指标
echo "friction 0 - 1"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 1 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction0.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 0 - 2"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 2 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction0.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 0 - 5"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 5 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction0.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 0 - 10"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 10 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction0.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 0 - 20"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 20 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction0.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 0 - 40"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 40 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction0.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 0 - 60"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 60 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction0.0-gravity9.81-object_height1.0 --test_rate_mode

echo "friction 1 - 0"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 0 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 1 - 2"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 2 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 1 - 5"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 5 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 1 - 10"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 10 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 1 - 20"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 20 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 1 - 40"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 40 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 1 - 60"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 60 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction1.0-gravity9.81-object_height1.0 --test_rate_mode

