# 예제 7-6 기본적인 C 타입을 지정하여 파이썬 가상 머신보다 C 코드로 더 많이 동작하도록 변경한 코드. 컴파일된 함수가 더 빠르다.

def calculate_z(int maxiter, zs, cs):
    """ 쥘리아 업데이트 규칙을 이용해 output 리스트를 계산한다. """
    cdef unsigned int i, n
    cdef double complex z, c
    output = [0] * len(zs)
    for i in range(len(zs)):
        n=0
        z = zs[i]
        c = cs[i]
        while n < maxiter and abs(z) < 2:
            z = z * z + c
            n += 1
        output[i] = n
    return output
