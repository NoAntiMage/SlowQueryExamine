# coding: utf-8
import pymysql
import yaml


class QueryTime(object):
    sql_time = "SELECT curtime(6);"

    def __init__(self, config_file='./config.yaml'):
        self.config_file = config_file
        self._db_config = self.get_yaml_data(self.config_file)
        self._db = pymysql.connect(**self._db_config['config'])
        self.cursor = self._db.cursor()

    @staticmethod
    def get_yaml_data(yaml_file):
        with open(yaml_file, 'rb') as f:
            file_data = f.read()
        # print(file_data)
        data = yaml.load(file_data, Loader=yaml.FullLoader)
        return data

    def get_query_time(self, sql):
        self.cursor.execute(self.sql_time)
        begin_at = self.cursor.fetchone()[0]
        self.cursor.execute(sql)
        self.cursor.execute(self.sql_time)
        end_at = self.cursor.fetchone()[0]
        duration = end_at - begin_at
        self.cursor.execute('SELECT sleep(0.3);')
        return str(duration)


if __name__ == '__main__':
    sql = 'SELECT VERSION();'
    query_time = QueryTime()

    spend_time = query_time.get_query_time(sql)
    print(spend_time)

# done 单次sql执行时间