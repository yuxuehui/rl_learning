

current_time=$(date "+%Y-%m-%d %H:%M:%S")
echo "The current time is: $current_time"


nohup python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 0 > out/PandaPush_friction_0_$current_time.out &

nohup python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 0.1 > out/PandaPush_friction_0.1_$current_time.out &

nohup python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 0.2 > out/PandaPush_friction_0.2_$current_time.out &

nohup python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 0.5 > out/PandaPush_friction_0.5_$current_time.out &

nohup python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 1 > out/PandaPush_friction_1_$current_time.out &


nohup python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 2 > out/PandaPush_friction_2_$current_time.out &

nohup python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 5 > out/PandaPush_friction_5_$current_time.out &

nohup python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 10 > out/PandaPush_friction_10_$current_time.out &

nohup python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 15 > out/PandaPush_friction_15_$current_time.out &

nohup python panda_sac.py --domain_name PandaPush-v3 --test_lateral_friction 20 > out/PandaPush_friction_20_$current_time.out &
