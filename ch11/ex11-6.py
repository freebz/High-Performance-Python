# 예제 11-6 numpy 배열에 더 복잡한 타입 지정하기

In [1]: %load_ext memory_profiler
In [2]: import numpy as np
In [3]: %memit arr=np.zeros(1e8, np.complex128)
peak memory: 1552.48 MiB, increment: 1525.75 MiB
In [4]: arr.size # len(arr)와 동일
Out[4]: 100000000
In [5]: arr.nbytes
Out[5]: 1600000000
In [6]: arr.nbytes/arr.size # 원소당 바이트 수
Out[6]: 16
In [7]: arr.itemsize # 원소 크기를 검사하는 다른 방법
Out[7]: 16
