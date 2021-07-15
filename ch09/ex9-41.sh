# 예제 9-41 Lock을 사용해 Value에 대한 쓰기를 동기화하기

# 변경에 대해 락을 걸었지만, 원자적이지는 않다.
$ python ex2_lock.py
Expecting to see a count of 4000
We have counted to 4000

$ python -m timeit -s "import ex2_lock" "ex2_lock.run_workers()"
10 loops, best of 3: 22.2 mesc per loop
