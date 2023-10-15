
nohup python panda_sac.py --domain_name PandaPush-v3 --test_gravity -19.6 > PandaPush_gravity_2g.out &

nohup python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_gravity -19.6 > PandaPickAndPlace_gravity_2g.out &

nohup python panda_sac.py --domain_name PandaPush-v3 --test_gravity -4.9 > PandaPush_gravity_0.5g.out &

nohup python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_gravity -4.9 > PandaPickAndPlace_gravity_0.5g.out &

nohup python panda_sac.py --domain_name PandaPush-v3 --test_gravity -0.0 > PandaPush_gravity_0g.out &

nohup python panda_sac.py --domain_name PandaPickAndPlace-v3 --test_gravity -0.0 > PandaPickAndPlace_gravity_0g.out &
