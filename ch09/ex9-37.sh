# 예제 9-37 락을 사용해 프로세스 4개에서 파일 기반의 횟수 세기를 실행한 경우의 타이밍

$ python ex_lock.py
Starting 4 process(es) to count to 4000
File is empty, starting to count from 0,
error: invlid literal for int() with base 10: ''
Expecting to see a count of 4000
count.txt contains:
4000

$ python -m timeit -s "import ex_lock" "ex_lock.run_workers()"
10 loops, best of 3: 401 mesc per loop
