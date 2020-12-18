# encoding: utf-8
# description: python output_turn_to_sql.py > ./output/slow_query.sql

import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')


with open('./output/slow_query.json') as f:
    data = json.load(f)

length = len(data)

n = 0
for i in range(1, length + 1):
    instance = data[str(i)]
    if instance['query_time_in_test'] > 3:
        n += 1
        print('-- NO {}'.format(n))
        print("-- query_time: {}\n-- rows_examined: {}\n-- rows_sent:{}\n-- lock_time: {}\n-- query_time_in_test: {}\n".format(instance['query_time'],instance['rows_examined'],instance['rows_sent'],instance['lock_time'],instance['query_time_in_test']))
        print(instance['sql'])
        print('\n' * 3)
