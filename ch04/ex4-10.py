# 예제 4-10 루프 안에서 느린 네임스페이스 탐색의 효과

from math import sin

def tight_loop_slow(iterations):
    """
    >>> %timeit tight_loop_slow(10000000)
    1 loops, best of 3: 2.21 s per loop
    """
    result = 0
    for in range(iterations):
        # sin 호출은 전역 네임스페이스에서 찾는다.
        result += sin(i)

def tight_loop_fast(iterations):
    """
    >>> %timeit tight_loop_fast(10000000)
    1 loops, best of 3: 2.02 s per loop
    """
    result = 0
    local_sin = sin
    for i in range(iterations):
        # local_sin 호출은 로컬 네임스페이스에서 찾는다.
        result += local_sin(i)
