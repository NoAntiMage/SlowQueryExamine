# coding: utf-8

import json
from parse_sql_log import ParseSqlLog
from execute_sql import QueryTime


class AllSqlUnitTest(object):
    def __init__(self):
        self.slow_query_list = list()

    def get_slow_query_list(self):
        log_parse = ParseSqlLog()
        sqlobj_list = log_parse.parse_slow_sql_file()
        query_time = QueryTime()
        # n = 0
        for sql_obj in sqlobj_list:
            try:
                # sql语句过长 视为异常sql
                if len(sql_obj.sql) <= log_parse.sql_char_limit:
                    duration = query_time.get_query_time(sql_obj.sql)
                else:
                    duration = 99.999
                    print('sql is to long')
        #
                sql_obj.query_time_in_test = duration
                self.slow_query_list.append(sql_obj)
        #         n += 1
            except Exception as e:
                # print(repr(e))
                continue

    def output_to_file_json(self):
        querys_dict = dict()
        num = 0
        for q in self.slow_query_list:
            num += 1
            querys_dict.update({num: q.__dict__})
        with open('./output/slow_query.json', 'w') as f:
            json.dump(querys_dict, f, default=str, indent=4)


if __name__ == '__main__':
    unittest = AllSqlUnitTest()
    unittest.get_slow_query_list()
    unittest.output_to_file_json()


# done 于mysql实例 执行 慢sql 获取 串行执行的执行时间
