# 예제 11-1 리스트에 같은 정수를 1억 개 저장하는 경우의 메모리 사용량 측정하기

In [1]: %load_ext memory_profiler # %memit 매직 함수를 로드한다.
In [2]: %memit [0]*int(1e8)
peak memory: 790.64 MiB, increment: 762.91 MiB
