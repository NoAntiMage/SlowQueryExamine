# /usr/bin/python
# coding: utf-8

from entity.SlowQuery import SlowQueryModel
from util.tool import get_yaml_data


class ParseSqlLog(object):
    def __init__(self, config_file='./config/scan_config.yaml'):
        self.config_file = config_file
        self.log_file = get_yaml_data(self.config_file)['config']['scan_log_file']
        self.scan_num = get_yaml_data(self.config_file)['config']['scan_line_num']
        self.sql_list = list()
        self._sql_set = set()
        self._line = str()
        self._sql = SlowQueryModel()
        self._flag = bool()

    def _get_single_sql(self):
        self._sql.sql += self._line

    def _parse_sql_info(self):
        sql_instance = SlowQueryModel()

        result = self._line.strip('# ').strip('\n').split(' ')
        sql_instance.query_time = result[1]
        sql_instance.lock_time = result[4]
        sql_instance.rows_sent = result[6]
        sql_instance.rows_examined = result[9]
        return sql_instance

    def _add_one_distinct_sql(self):
        self._sql_set.add(self._sql.sql)
        self.sql_list.append(self._sql)

    def parse_slow_sql_file(self):
        with open(self.log_file, 'rb') as f:
            num = 0
            sql_num = 0
            while True:
                num += 1
                self._line = f.readline()
                # Query_time行 记录了sql语句执行信息
                if 'Query_time:' in self._line:
                    self._sql = self._parse_sql_info()
                # SET行 开始加载sql
                if 'SET' in self._line:
                    self._flag = 1
                    continue
                # 至 # 号行结束
                if '#' in self._line and self._flag == 1:
                    self._flag = 0
                    sql_num += 1
                    # sql去重
                    if self._sql.sql not in self._sql_set:
                        self._add_one_distinct_sql()
                        self._sql = SlowQueryModel()
                    else:
                        self._sql = SlowQueryModel()
                        continue

                if self._flag == 1:
                    self._get_single_sql()
                if num == self.scan_num:
                    break
                if len(self._line) == 0:
                    break
            print(str(sql_num) + ' sql have been scan.')
            print(str(len(self.sql_list)) + ' distinct sql have been got.')
        return self.sql_list


if __name__ == '__main__':
    sql_parse = ParseSqlLog()
    results = sql_parse.parse_slow_sql_file()
    for s in results:
        print(s)

# done 完成日志 sql解析