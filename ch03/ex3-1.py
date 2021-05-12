# 예제 3-1 크기가 다른 리스트에서 항목을 읽는 데 걸린 시간

>>> %%timeit l = range(10)
        ...: l[5]
        ...:
10000000 loops, best of 3: 75.5 ns per loop
>>>
>>> %%timeit l = range(10000000)
        ...: l[100000]
        ...:
10000000 loops, best of 3: 76.3 ns per loop
