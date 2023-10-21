# 计算 mass 的指标
python panda_sac.py --domain_name PandaPush-v3 --test_mass 20 --test_model_path checkpoints/SAC-PandaPush-v3-mass20-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
python panda_sac.py --domain_name PandaPush-v3 --test_mass 40 --test_model_path checkpoints/SAC-PandaPush-v3-mass40-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
python panda_sac.py --domain_name PandaPush-v3 --test_mass 60 --test_model_path checkpoints/SAC-PandaPush-v3-mass60-friction1.0-gravity9.81-object_height1.0 --test_rate_mode

# 计算其他对比指标
echo "mass 1 - 20"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 20 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
echo "mass 1 - 40"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 40 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
echo "mass 1 - 60"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 60 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction1.0-gravity9.81-object_height1.0 --test_rate_mode

echo "mass 20 - 1"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 1 --test_model_path checkpoints/SAC-PandaPush-v3-mass20-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
echo "mass 20 - 40"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 40 --test_model_path checkpoints/SAC-PandaPush-v3-mass20-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
echo "mass 20 - 60"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 60 --test_model_path checkpoints/SAC-PandaPush-v3-mass20-friction1.0-gravity9.81-object_height1.0 --test_rate_mode

echo "mass 40 - 1"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 1 --test_model_path checkpoints/SAC-PandaPush-v3-mass40-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
echo "mass 40 - 20"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 20 --test_model_path checkpoints/SAC-PandaPush-v3-mass40-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
echo "mass 40 - 60"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 60 --test_model_path checkpoints/SAC-PandaPush-v3-mass40-friction1.0-gravity9.81-object_height1.0 --test_rate_mode

echo "mass 60 - 1"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 1 --test_model_path checkpoints/SAC-PandaPush-v3-mass60-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
echo "mass 60 - 20"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 20 --test_model_path checkpoints/SAC-PandaPush-v3-mass60-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
echo "mass 60 - 40"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 40 --test_model_path checkpoints/SAC-PandaPush-v3-mass60-friction1.0-gravity9.81-object_height1.0 --test_rate_mode

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

echo "friction 2 - 0"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 0 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction2.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 2 - 1"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 1 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction2.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 2 - 5"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 5 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction2.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 2 - 10"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 10 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction2.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 2 - 20"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 20 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction2.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 2 - 40"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 40 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction2.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 2 - 60"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 60 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction2.0-gravity9.81-object_height1.0 --test_rate_mode

echo "friction 5 - 0"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 0 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction5.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 5 - 1"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 1 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction5.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 5 - 2"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 2 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction5.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 5 - 10"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 10 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction5.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 5 - 20"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 20 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction5.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 5 - 40"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 40 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction5.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 5 - 60"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 60 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction5.0-gravity9.81-object_height1.0 --test_rate_mode

echo "friction 10 - 0"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 0 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction10.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 10 - 1"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 1 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction10.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 10 - 2"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 2 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction10.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 10 - 5"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 5 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction10.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 10 - 20"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 20 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction10.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 10 - 40"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 40 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction10.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 10 - 60"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 60 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction10.0-gravity9.81-object_height1.0 --test_rate_mode

echo "friction 20 - 0"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 0 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction20.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 20 - 1"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 1 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction20.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 20 - 2"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 2 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction20.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 20 - 5"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 5 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction20.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 20 - 10"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 10 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction20.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 20 - 40"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 40 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction20.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 20 - 60"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 60 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction20.0-gravity9.81-object_height1.0 --test_rate_mode

echo "friction 40 - 0"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 0 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction40.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 40 - 1"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 1 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction40.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 40 - 2"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 2 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction40.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 40 - 5"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 5 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction40.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 40 - 10"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 10 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction40.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 40 - 20"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 20 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction40.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 40 - 60"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 60 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction40.0-gravity9.81-object_height1.0 --test_rate_mode

echo "friction 60 - 0"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 0 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction60.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 60 - 1"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 1 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction60.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 60 - 2"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 2 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction60.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 60 - 5"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 5 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction60.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 60 - 10"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 10 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction60.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 60 - 20"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 20 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction60.0-gravity9.81-object_height1.0 --test_rate_mode
echo "friction 60 - 40"
python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 40 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction60.0-gravity9.81-object_height1.0 --test_rate_mode

