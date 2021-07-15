# 예제 9-39 락을 사용하지 않아서 잘못된 카운터 값이 나온 경우

$ python ex2_nolock.py
Expecting to see a count of 4000
We have counted to 2340

$ python -m timeit -s "import ex2_nolock" "ex2_nolock.run_workers()"
100 loops, best of 3: 12.6 mesc per loop
