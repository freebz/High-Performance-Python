# 예제 11-7 파이썬 2.7에서는 유니코드 객체의 비용이 비싸다.

In [1]: %load_ext memory_profiler
In [2]: %memit b"a" * int(1e8)
peak memory: 100.98 MiB, increment: 80.97 MiB
In [3]: %memit u"a" * int(1e8)
peak memory: 380.98 MiB, increment: 360.92 MiB
