# 예제 6-13 제자리 연산으로 메모리 할당 줄이기

>>> %%timeit array1, array2 = np.random.random((10,10)), np.random.random((10,10))
... array1 = array1 + array2
...
100000 loops, best of 3: 3.03 us per loop

>>> %%timeit array1, array2 = np.random.random((10,10)), np.random.random((10,10))
... array1 += array2
...
100000 loops, best of 3: 2.42 us per loop
