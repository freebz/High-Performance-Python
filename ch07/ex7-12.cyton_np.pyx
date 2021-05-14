# 예제 7-12 OpenMP로 병렬화하기 위해 ㅔㄱ뭏ㄷ 추가하기

# cython_np.pyx
from cython.parallel import prange
import numpy as np
cimport numpy as np

def calculate_z(int maxiter, double complex[:] zs, double complex[:] cs):
    """ 쥘리아 업데이트 규칙을 이용해 output 리스트를 계산한다. """
    cdef unsigned int i, length
    cdef double complex z, c
    cdef int[:] output = np.empty(len(zs), dtype=np.int32)
        length = len(zs)
    with nogil:
        for i in prange(length, schedule="guided"):
            z = zs[i]
            c = cs[i]
            output[i] = 0
            while output[i] < maxiter and (z.real * z.real + z.imag * z.imag) < 4:
                z=z*z+c
                output[i] += 1
    return output
