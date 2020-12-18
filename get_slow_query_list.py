# coding: utf-8

import json
from parse_sql_log import ParseSqlLog
from execute_sql import QueryTime


def get_slow_query_list():
    l = list()
    log_parse = ParseSqlLog(log_file='./slow_sql/mysql_slow.log', scan_num=1000)
    sql_list = log_parse.parse_slow_sql_file()
    query_time = QueryTime()
    n = 0
    for sql_obj in sql_list:
        try:
            # print(sql_obj.sql)
            # sql语句过长 视为异常sql
            if len(sql_obj.sql) <= 10000:
                duration = query_time.get_query_time(sql_obj.sql)

            else:
                duration = '99.999'
                print('sql is to long')

            sql_obj.query_time_in_test = duration.split(":")[-1].strip('0')
            # print(sql_obj)
            l.append(sql_obj)
            n += 1
        except Exception as e:
            # print(e)
            continue
    return l


if __name__ == '__main__':
    slow_query_list = get_slow_query_list()
    for sql_obj in slow_query_list:
        print(sql_obj)


# done 于mysql实例 执行 慢sql 获取 串行执行的执行时间