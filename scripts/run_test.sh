# mass-h-0.7-2.7
# 计算 mass 的指标


# 计算 mass 的指标
echo "mass 1"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 1 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass1-friction1.0-gravity9.81-object_height1.0-2023-11-15-02:13:47-702338 --test_rate_mode

echo "mass 2"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 2 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass2-friction1.0-gravity9.81-object_height1.0-2023-11-15-02:13:47-742244 --test_rate_mode

echo "mass 5"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 5 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass5-friction1.0-gravity9.81-object_height1.0-2023-11-15-02:13:47-597162 --test_rate_mode

echo "mass 10"
python panda_sac.py --domain_name PandaPush-v3 --test_mass 10 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass10-friction1.0-gravity9.81-object_height1.0-2023-11-15-02:13:47-701661 --test_rate_mode

# 计算 mass 的指标
echo "mass 1"
python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 1 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass1-friction1.0-gravity9.81-object_height1.0-2023-11-15-02:13:47-702338 --test_rate_mode

echo "mass 2"
python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 2 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass2-friction1.0-gravity9.81-object_height1.0-2023-11-15-02:13:47-742244 --test_rate_mode

echo "mass 5"
python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 5 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass5-friction1.0-gravity9.81-object_height1.0-2023-11-15-02:13:47-597162 --test_rate_mode

echo "mass 10"
python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 10 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass10-friction1.0-gravity9.81-object_height1.0-2023-11-15-02:13:47-701661 --test_rate_mode


# # 计算其他对比指标
# echo "mass 1 - 2"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 2 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass1-friction1.0-gravity9.81-object_height1.0-2023-11-15-02:13:47-702338 --test_rate_mode
# echo "mass 1 - 5"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 5 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass1-friction1.0-gravity9.81-object_height1.0-2023-11-15-02:13:47-702338 --test_rate_mode
# echo "mass 1 - 10"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 10 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass1-friction1.0-gravity9.81-object_height1.0-2023-11-15-02:13:47-702338 --test_rate_mode

# # 计算其他对比指标
# echo "mass 2 - 1"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 1 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass2-friction1.0-gravity9.81-object_height1.0-2023-11-15-02:13:47-742244 --test_rate_mode
# echo "mass 2 - 5"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 5 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass2-friction1.0-gravity9.81-object_height1.0-2023-11-15-02:13:47-742244 --test_rate_mode
# echo "mass 2 - 10"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 10 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass2-friction1.0-gravity9.81-object_height1.0-2023-11-15-02:13:47-742244 --test_rate_mode

# # 计算其他对比指标
# echo "mass 5 - 1"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 1 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass5-friction1.0-gravity9.81-object_height1.0-2023-11-15-02:13:47-597162 --test_rate_mode
# echo "mass 5 - 2"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 2 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass5-friction1.0-gravity9.81-object_height1.0-2023-11-15-02:13:47-597162 --test_rate_mode
# echo "mass 5 - 10"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 10 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass5-friction1.0-gravity9.81-object_height1.0-2023-11-15-02:13:47-597162 --test_rate_mode

# # 计算其他对比指标
# echo "mass 10 - 1"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 1 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass10-friction1.0-gravity9.81-object_height1.0-2023-11-15-02:13:47-701661 --test_rate_mode
# echo "mass 10 - 2"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 2 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass10-friction1.0-gravity9.81-object_height1.0-2023-11-15-02:13:47-701661 --test_rate_mode
# echo "mass 10 - 5"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 5 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass10-friction1.0-gravity9.81-object_height1.0-2023-11-15-02:13:47-701661 --test_rate_mode



# echo "mass 1"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 1 --test_model_path checkpoints/mass-h-0.7-2.7/SAC-PandaPickAndPlace-v3-mass1-friction1.0-gravity9.81-object_height1.0 --test_rate_mode

# echo "mass 2"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 2 --test_model_path checkpoints/mass-h-0.7-2.7/SAC-PandaPickAndPlace-v3-mass2-friction1.0-gravity9.81-object_height1.0 --test_rate_mode

# echo "mass 5"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 5 --test_model_path checkpoints/mass-h-0.7-2.7/SAC-PandaPickAndPlace-v3-mass5-friction1.0-gravity9.81-object_height1.0 --test_rate_mode

# echo "mass 10"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 10 --test_model_path checkpoints/mass-h-0.7-2.7/SAC-PandaPickAndPlace-v3-mass10-friction1.0-gravity9.81-object_height1.0 --test_rate_mode

# # 计算 mass 的指标
# echo "mass 1"
# python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 1 --test_model_path checkpoints/mass-h-0.7-2.7/SAC-PandaPickAndPlace-v3-mass1-friction1.0-gravity9.81-object_height1.0 --test_rate_mode

# echo "mass 2"
# python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 2 --test_model_path checkpoints/mass-h-0.7-2.7/SAC-PandaPickAndPlace-v3-mass2-friction1.0-gravity9.81-object_height1.0 --test_rate_mode

# echo "mass 5"
# python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 5 --test_model_path checkpoints/mass-h-0.7-2.7/SAC-PandaPickAndPlace-v3-mass5-friction1.0-gravity9.81-object_height1.0 --test_rate_mode

# echo "mass 10"
# python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 10 --test_model_path checkpoints/mass-h-0.7-2.7/SAC-PandaPickAndPlace-v3-mass10-friction1.0-gravity9.81-object_height1.0 --test_rate_mode


# # 计算其他对比指标
# echo "mass 1 - 2"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 2 --test_model_path checkpoints/mass-h-0.7-2.7/SAC-PandaPickAndPlace-v3-mass1-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
# echo "mass 1 - 5"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 5 --test_model_path checkpoints/mass-h-0.7-2.7/SAC-PandaPickAndPlace-v3-mass1-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
# echo "mass 1 - 10"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 10 --test_model_path checkpoints/mass-h-0.7-2.7/SAC-PandaPickAndPlace-v3-mass1-friction1.0-gravity9.81-object_height1.0 --test_rate_mode

# # 计算其他对比指标
# echo "mass 2 - 1"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 1 --test_model_path checkpoints/mass-h-0.7-2.7/SAC-PandaPickAndPlace-v3-mass2-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
# echo "mass 2 - 5"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 5 --test_model_path checkpoints/mass-h-0.7-2.7/SAC-PandaPickAndPlace-v3-mass2-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
# echo "mass 2 - 10"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 10 --test_model_path checkpoints/mass-h-0.7-2.7/SAC-PandaPickAndPlace-v3-mass2-friction1.0-gravity9.81-object_height1.0 --test_rate_mode

# # 计算其他对比指标
# echo "mass 5 - 1"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 1 --test_model_path checkpoints/mass-h-0.7-2.7/SAC-PandaPickAndPlace-v3-mass5-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
# echo "mass 5 - 2"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 2 --test_model_path checkpoints/mass-h-0.7-2.7/SAC-PandaPickAndPlace-v3-mass5-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
# echo "mass 5 - 10"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 10 --test_model_path checkpoints/mass-h-0.7-2.7/SAC-PandaPickAndPlace-v3-mass5-friction1.0-gravity9.81-object_height1.0 --test_rate_mode

# # 计算其他对比指标
# echo "mass 10 - 1"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 1 --test_model_path checkpoints/mass-h-0.7-2.7/SAC-PandaPickAndPlace-v3-mass10-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
# echo "mass 10 - 2"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 2 --test_model_path checkpoints/mass-h-0.7-2.7/SAC-PandaPickAndPlace-v3-mass10-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
# echo "mass 10 - 5"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 5 --test_model_path checkpoints/mass-h-0.7-2.7/SAC-PandaPickAndPlace-v3-mass10-friction1.0-gravity9.81-object_height1.0 --test_rate_mode


# # 计算 mass 的指标
# echo "mass 1"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 1 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass1-friction1.0-gravity9.81-object_height1.0-2023-11-04-23:19:57-205074 --test_rate_mode

# echo "mass 2"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 2 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass2-friction1.0-gravity9.81-object_height1.0-2023-11-04-23:19:57-175596 --test_rate_mode

# echo "mass 5"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 5 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass5-friction1.0-gravity9.81-object_height1.0-2023-11-04-23:19:57-270143 --test_rate_mode

# echo "mass 10"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 10 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass10-friction1.0-gravity9.81-object_height1.0-2023-11-05-10:19:22-943333 --test_rate_mode

# # 计算 mass 的指标
# echo "mass 1"
# python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 1 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass1-friction1.0-gravity9.81-object_height1.0-2023-11-04-23:19:57-205074 --test_rate_mode

# echo "mass 2"
# python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 2 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass2-friction1.0-gravity9.81-object_height1.0-2023-11-04-23:19:57-175596 --test_rate_mode

# echo "mass 5"
# python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 5 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass5-friction1.0-gravity9.81-object_height1.0-2023-11-04-23:19:57-270143 --test_rate_mode

# echo "mass 10"
# python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 10 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass10-friction1.0-gravity9.81-object_height1.0-2023-11-05-10:19:22-943333 --test_rate_mode


# # 计算其他对比指标
# echo "mass 1 - 2"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 2 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass1-friction1.0-gravity9.81-object_height1.0-2023-11-04-23:19:57-205074 --test_rate_mode
# echo "mass 1 - 5"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 5 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass1-friction1.0-gravity9.81-object_height1.0-2023-11-04-23:19:57-205074 --test_rate_mode
# echo "mass 1 - 10"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 10 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass1-friction1.0-gravity9.81-object_height1.0-2023-11-04-23:19:57-205074 --test_rate_mode

# # 计算其他对比指标
# echo "mass 2 - 1"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 1 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass2-friction1.0-gravity9.81-object_height1.0-2023-11-04-23:19:57-175596 --test_rate_mode
# echo "mass 2 - 5"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 5 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass2-friction1.0-gravity9.81-object_height1.0-2023-11-04-23:19:57-175596 --test_rate_mode
# echo "mass 2 - 10"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 10 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass2-friction1.0-gravity9.81-object_height1.0-2023-11-04-23:19:57-175596 --test_rate_mode

# # 计算其他对比指标
# echo "mass 5 - 1"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 1 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass5-friction1.0-gravity9.81-object_height1.0-2023-11-04-23:19:57-270143 --test_rate_mode
# echo "mass 5 - 2"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 2 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass5-friction1.0-gravity9.81-object_height1.0-2023-11-04-23:19:57-270143 --test_rate_mode
# echo "mass 5 - 10"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 10 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass5-friction1.0-gravity9.81-object_height1.0-2023-11-04-23:19:57-270143 --test_rate_mode

# # 计算其他对比指标
# echo "mass 10 - 1"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 1 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass10-friction1.0-gravity9.81-object_height1.0-2023-11-05-10:19:22-943333 --test_rate_mode
# echo "mass 10 - 2"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 2 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass10-friction1.0-gravity9.81-object_height1.0-2023-11-05-10:19:22-943333 --test_rate_mode
# echo "mass 10 - 5"
# python panda_sac.py --domain_name PandaPush-v3 --test_mass 5 --test_model_path checkpoints/SAC-PandaPickAndPlace-v3-mass10-friction1.0-gravity9.81-object_height1.0-2023-11-05-10:19:22-943333 --test_rate_mode



# # 计算其他对比指标
# echo "friction 0 - 1"
# python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 1 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction0.0-gravity9.81-object_height1.0 --test_rate_mode
# echo "friction 0 - 2"
# python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 2 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction0.0-gravity9.81-object_height1.0 --test_rate_mode
# echo "friction 0 - 5"
# python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 5 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction0.0-gravity9.81-object_height1.0 --test_rate_mode
# echo "friction 0 - 10"
# python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 10 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction0.0-gravity9.81-object_height1.0 --test_rate_mode
# echo "friction 0 - 20"
# python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 20 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction0.0-gravity9.81-object_height1.0 --test_rate_mode
# echo "friction 0 - 40"
# python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 40 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction0.0-gravity9.81-object_height1.0 --test_rate_mode
# echo "friction 0 - 60"
# python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 60 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction0.0-gravity9.81-object_height1.0 --test_rate_mode

# echo "friction 1 - 0"
# python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 0 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
# echo "friction 1 - 2"
# python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 2 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
# echo "friction 1 - 5"
# python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 5 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
# echo "friction 1 - 10"
# python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 10 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
# echo "friction 1 - 20"
# python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 20 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
# echo "friction 1 - 40"
# python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 40 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction1.0-gravity9.81-object_height1.0 --test_rate_mode
# echo "friction 1 - 60"
# python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 60 --test_model_path checkpoints/SAC-PandaPush-v3-mass1.0-friction1.0-gravity9.81-object_height1.0 --test_rate_mode

