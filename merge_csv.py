import csv
import os
import glob
import re
from datetime import datetime
import copy

from utils import states_to_result

def re_match(csv_name):
    """
    algorithm: r'train-(.*?)-'
    train_domain: r'train-.*?-(.*?)-'
    train_mass: r'train.*?mass(.*?)-.*?test'
    train_friction: r'train.*?friction(.*?)-.*?test'
    train_gravity: r'train.*?gravity(.*?)-.*?test'
    train_object_height: r'train.*?object_height(.*?)-.*?test'
    test_domain: r'test-(.*?)-'
    test_mass: r'test.*?mass(.*?)-'
    test_friction: r'test.*?friction(.*?)-'
    test_gravity: r'test.*?gravity(.*?)-'
    test_object_height: r'test.*?object_height(.*?)-'
    date: r'(\d\d\d\d-\d\d-\d\d-\d\d:\d\d:\d\d-\d\d\d\d\d\d)'

    """
    def _extract(pattern, string, default = ''):
        ans = re.search(pattern, string)
        if ans is None: return default
        else: return ans.group(1)

    algorithm = _extract(r'train-(.*?)-',csv_name,'SAC')
    train_domain = _extract(r'train-.*?-(.*?)-',csv_name)
    train_mass = float(_extract(r'train.*?mass(.*?)-.*?test',csv_name,'1.0'))
    train_friction = float(_extract(r'train.*?friction(.*?)-.*?test',csv_name,'1.0'))
    train_gravity = float(_extract(r'train.*?gravity(.*?)-.*?test',csv_name,'9.81'))
    train_object_height = float(_extract(r'train.*?object_height(.*?)-.*?test',csv_name,'1.0'))
    test_domain = _extract(r'test-(.*?)-',csv_name)
    test_mass = float(_extract(r'test.*?mass(.*?)-',csv_name,'1.0'))
    test_friction = float(_extract(r'test.*?friction(.*?)-',csv_name,'1.0'))
    test_gravity = float(_extract(r'test.*?gravity(.*?)-',csv_name,'9.81'))
    test_object_height = float(_extract(r'test.*?object_height(.*?)-',csv_name,'1.0'))
    date = datetime.strptime(_extract(r'(\d\d\d\d-\d\d-\d\d-\d\d:\d\d:\d\d-\d\d\d\d\d\d)',csv_name,'2023-10-01-00:00:00-000000'),"%Y-%m-%d-%H:%M:%S-%f").date()
    return locals()

def merge_csv(csv_path,out_path):
    csv_files = glob.glob(os.path.join(csv_path,'*.csv'))
    ignore_keys = ['csv_name','_extract','date']

    def _encode(_data):
        ans = []
        for key in _data:
            if key in ignore_keys: continue
            ans.append(str(_data[key]))
        return '-'.join(ans)

    with open(out_path,'w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        head = ['algorithm','train_domain','train_mass','train_friction','train_gravity','train_object_height',
                 'test_domain','test_mass','test_friction','test_gravity','test_object_height',
                 'push_rate','roll_rate','pickandplace_rate','success_rate']
        experiment_result = {}

        for csv_file in csv_files:

            # 统计完成每个任务的比率
            count = {'push':0,'roll':0,'pickandplace':0,'success':0}
            with open(csv_file,'r',encoding='utf-8') as f:
                reader = csv.reader(f)
                for states in reader:
                    result = states_to_result(states)
                    count[result] += 1
                    if states[-1] == 'success': count['success'] += 1

            all_num = count['push'] + count['roll'] + count['pickandplace']
            push_rate = count['push'] / all_num
            roll_rate = count['roll'] / all_num
            pickandplace_rate = count['pickandplace'] / all_num
            success_rate = count['success'] / all_num

            # 记录实验结果
            experiment_name = csv_file.split('/')[-1].replace('.csv','')
            experiment_state = re_match(experiment_name)
            experiment_code = _encode(experiment_state)
            if experiment_code not in experiment_result or experiment_result[experiment_code][0]['date'] < experiment_state['date']:
                experiment_result[experiment_code] = [experiment_state,push_rate,roll_rate,pickandplace_rate,success_rate]

        data = []
        for item in experiment_result.values():
            _data = []
            # print(item)
            for key in item[0]:
                if key in ignore_keys: continue
                _data.append(item[0][key])
            _data.extend(item[1:])
            data.append(_data)

        data.sort()
        data = [head] + data
        writer.writerows(data)

if __name__ == '__main__':
    merge_csv('./csv','merge.csv')
    

