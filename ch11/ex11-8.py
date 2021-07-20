# 예제 11-8 파이썬 3.3 이상에서는 유니코드 객체가 훨씬 싸다

Python 3.3.2+ (default, Oct 9 2013, 14:50:09)
IPython 1.2.0 - An enhanced Interactive Python.
...
In [1]: %load_ext memory_profiler
In [2]: %memit b"a" * int(1e8)
peak memory: 91.77 MiB, increment: 71.41 MiB
In [3]: %memit u"a" * int(1e8)
peak memory: 91.54 MiB, increment: 70.98 MiB
In [4]: %memit u"Σ" * int(1e8)
peak memory: 174.72 MiB, increment: 153.76 MiB
