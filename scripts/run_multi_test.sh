
current_time=$(date "+%Y-%m-%d %H:%M:%S")
echo "The current time is: $current_time"

nohup python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 1 > PandaPickAndPlace_mass_1_$current_time.out &
# nohup python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 10 > PandaPickAndPlace_mass_10_$current_time.out &

nohup python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 1.0 > PandaPush_friction_1_$current_time.out &
# nohup python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 20 > PandaPickAndPlace_mass_20_$current_time.out &

nohup python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 5.0 > PandaPush_friction_5_$current_time.out &
# nohup python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 20 > PandaPickAndPlace_mass_20_$current_time.out &
