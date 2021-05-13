# 예제 5-2 필요할 때만 데이터 읽기

from random import normalvariate, rand
from itertools import count

def read_data(filename):
    with open(filename) as fd:
        for line in fd:
            data = line.strip().split(',')
            yield list(map(int, data))

def read_fake_data(filename):
    for i in count():
        sigma = rand() * 10
        yield (i, normalvariate(0, sigma))
