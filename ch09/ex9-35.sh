# 예제 9-35 락이 없이 프로세스 4개에서 파일 기반의 횟수 세기를 실행한 경우의 타이밍

$ python ex1_nolock.py
Starting 4 process(es) to count to 4000
File is empty, starting to count from 0.
error: invlid literal for int() with base 10: ''
File is empty, starting to count from 0.
error: invlid literal for int() with base 10: '1\n7\n'
# many errors like these
Expecting to see a count of 4000
count.txt contains:
629

$ python -m timeit -s "import ex1_nolock" "ex_nolock.run_workers()"
10 loops, best of 3: 125 msec per loop
