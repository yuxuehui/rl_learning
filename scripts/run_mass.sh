#!/bin/bash

current_time=$(date "+%Y-%m-%d %H:%M:%S")
echo "The current time is: $current_time"

nohup python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 1 > out/PandaPickAndPlace_mass_1_$current_time.out &
# nohup python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 10 > PandaPickAndPlace_mass_10_$current_time.out &

nohup python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 2 > out/PandaPickAndPlace_mass_2_$current_time.out &
# nohup python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 20 > PandaPickAndPlace_mass_20_$current_time.out &

nohup python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 5 > out/PandaPickAndPlace_mass_5_$current_time.out &
# nohup python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 50 > PandaPickAndPlace_mass_50_$current_time.out &

nohup python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 10 > out/PandaPickAndPlace_mass_10_$current_time.out &
# nohup python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_mass 100 > PandaPickAndPlace_mass_100_$current_time.out &
