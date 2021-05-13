# 예제 5-3 데이터 그룹 만들기

from datetime import date
from itertools import groupby

def day_grouper(iterable):
    key = lambda (timestamp, value) : date.fromtimestamp(timestamp)
    return groupby(iterable, key)
