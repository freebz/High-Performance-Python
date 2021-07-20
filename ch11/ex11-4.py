# 예제 11-4 760MB의 RAM을 사용해 1억 개의 정수로 이뤄진 배열 만들기

In [1]: %load_ext memory_profiler
In [2]: import array
In [3]: %memit array.array('l', xrange(int(1e8)))
peak memory: 781.03 MiB, increment: 760.98 MiB
In [4]: arr = array.array('l')
In [5]: arr.itemsize
Out[5]: 8
