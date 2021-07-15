# 예제 9-44 RawValue와 Lock 방식이 더 빠르다

# RawValue에 대한 락은 없다.
$ python ex2_lock_rawvalue.py
Expecting to see a count of 4000
We have counted to 4000

$ python -m timeit -s "import ex2_lock_rawvalue" "ex2_lock_rawvalue.run_workers()"
100 loops, best of 3: 12.6 mesc per loop
