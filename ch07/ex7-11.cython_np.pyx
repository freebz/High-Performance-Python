# 예제 7-11 쥘리아 계산 함수의 애너테이션이 달린 numpy 버전

# cython_np.pyx
import numpy as np
cimport numpy as np

def calculate_z(int maxiter, double complex[:] zs, double complex[:] cs):
    """ 쥘리아 업데이트 규칙을 이용해 output 리스트를 계산한다. """
    cdef unsigned int i, n
    cdef double complex z, c
    cdef int[:] output = np.empty(len(zs), dtype=np.int32)
    for i in range(len(zs)):
        n=0
        z = zs[i]
        c = cs[i]
        while n < maxiter and (z.real * z.real + z.imag * z.imag) < 4:
            z=z*z+c
            n += 1
        output[i] = n
    return output
