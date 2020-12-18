# coding: utf-8


class SlowQueryModel(object):
    def __init__(self):
        self.sql = str()
        self.query_time = 0
        self.lock_time = 0
        self.rows_sent = str()
        self.rows_examined = str()
        self.query_time_in_test = 0

    def __str__(self):
        return 'query time : {}\nlock time: {}\nrows_sent: {}\nrows_examined: {}\nquery_time_in_test: {}\n\n'.format(str(self.query_time), self.lock_time, self.rows_sent, self.rows_examined, self.query_time_in_test)

