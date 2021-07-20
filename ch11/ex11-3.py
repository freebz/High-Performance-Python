# 예제 11-3 1억 개의 서로 다른 정수를 다시 한 번 저장하면서 메모리 사용량 측정하기

In [5]: %memit [n for n in xrange(int(1e8))]
peak memory: 3127.52 MiB, increment: 762.71 MiB
