# 예제 11-2 리스트에 1억 개의 서로 다른 정수를 저장하는 경우의 메모리 사용량 측정하기

# 메모리 상태를 초기화히기 위해 새로운 IPython 셀을 사용한다.
In [1]: %load_ext memory_profiler
In [2]: %memit # 이 프로세스가 현재 사용중인 RAM의 양을 보여준다.
peak memory: 20.05 MiB, increment: 0.03 MiB
In [3]: %memit [n for n in xrange(int(1e8))]
peak memory: 3127.53 MiB, increment: 3106.96 MiB
In [4]: %memit
peak memory: 2364.81 Mib, increment: 0.00 MiB
