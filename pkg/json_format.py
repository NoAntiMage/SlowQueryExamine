import json
from datetime import timedelta


# todo timedelta format
class TimedeltaEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, timedelta):
            pass
        else:
            return json.JSONEncoder.default(self, obj)
