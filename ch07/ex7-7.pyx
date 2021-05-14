# 예제 7-7 Cython을 이용한 abs 함수 확장

def calculate_z(int maxiter, zs, cs):
    """ 쥘리아 업데이트 규칙을 이용해 output 리스트를 계산한다. """
    cdef unsigned int i, n
    cdef double complex z, c
    output = [0] * len(zs)
    for i in range(len(zs)):
        n=0
        z = zs[i]
        c = cs[i]
        while n < maxiter and (z.real * z.real + z.imag * z.imag) < 4:
            z = z * z + c
            n += 1
        output[i] = n
    return output
