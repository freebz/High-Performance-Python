# 예제 2-18 %timeit으로 내장 함수를 사용한 코드가 더 빠를 것이라는 가설 검증

%timeit fn_expressive()
10 loops, best of 3: 42 ms per loop

%timeit fn_terse()
100 loops, best of 3: 12.3 ms per loop
