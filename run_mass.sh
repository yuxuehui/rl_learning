#!/bin/bash

current_time=$(date "+%Y-%m-%d %H:%M:%S")
echo "The current time is: $current_time"

nohup python panda_sac.py --domain_name PandaPush-v3 --test_mass 1 > PandaPush_mass_1_$current_time.out &
nohup python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 1 > PandaPickAndPlace_mass_1_$current_time.out &

nohup python panda_sac.py --domain_name PandaPush-v3 --test_mass 2 > PandaPush_mass_2_$current_time.out &
nohup python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 2 > PandaPickAndPlace_mass_2_$current_time.out &

nohup python panda_sac.py --domain_name PandaPush-v3 --test_mass 5 > PandaPush_mass_5_$current_time.out &
nohup python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 5 > PandaPickAndPlace_mass_5_$current_time.out &

nohup python panda_sac.py --domain_name PandaPush-v3 --test_mass 10 > PandaPush_mass_10_$current_time.out &
nohup python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 10 > PandaPickAndPlace_mass_10_$current_time.out &
