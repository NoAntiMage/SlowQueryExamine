# /usr/bin/python
# coding: utf-8


class ParseSqlLog(object):
    def __init__(self, log_file, scan_num=10**4):
        self.log_file = log_file
        self.scan_num = scan_num
        self.sql_set = set()
        self._line = str()
        self._sql = str()
        self._flag = bool()

    def get_single_sql(self):
        self._sql += self._line

    def parse_slow_sql_file(self):
        with open(self.log_file, 'rb') as f:
            num = 0
            sql_num = 0
            while True:
                num += 1
                self._line = f.readline()
                if 'SET' in self._line:
                    self._flag = 1
                    continue
                if '#' in self._line and self._flag == 1:
                    self._flag = 0
                    # print('------------- SQL query -------------')
                    # print(self._sql)
                    self.sql_set.add(self._sql)
                    self._sql = ''
                    sql_num += 1

                if self._flag == 1:
                    self.get_single_sql()
                if num == self.scan_num:
                    break
            print(str(sql_num) + ' sql have been scan.')
            print(str(len(self.sql_set)) + ' distinct sql have been got.')
        return self.sql_set


if __name__ == '__main__':
    sql_parse = ParseSqlLog(log_file='./slow_sql/mysql_slow.log', scan_num=1000)
    sql_parse.parse_slow_sql_file()
