# coding: utf-8

import json
from parse_sql_log import ParseSqlLog
from execute_sql import QueryTime
from entity.SlowQuery import SlowQuery


def get_slow_query_list():
    l = list()
    log_parse = ParseSqlLog(log_file='./slow_sql/mysql_slow.log', scan_num=1000)
    sql_set = log_parse.parse_slow_sql_file()
    query_time = QueryTime()
    for sql in sql_set:
        try:
            duration = query_time.get_query_time(sql)
            print(duration)
            slow_query = SlowQuery(sql, duration)
            l.append(slow_query)
        except Exception as e:
            # print(e)
            continue
    return l


if __name__ == '__main__':
    slow_query_list = get_slow_query_list()
    # for q in slow_query_list:
    #     print(q.duration)
    #     print(type(q.duration))

    querys_dict = dict()
    num = 0
    for q in slow_query_list:
        num += 1
        querys_dict.update({num: q.__dict__})
    with open('./output/slow_query.json', 'w') as f:
        json.dump(querys_dict, f, default=str, indent=4)
