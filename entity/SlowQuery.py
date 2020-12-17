# coding: utf-8


class SlowQuery(object):
    def __init__(self, sql, duration):
        self.sql = sql
        self.duration = duration

    def __str__(self):
        return 'query time : ' + str(self.duration)

