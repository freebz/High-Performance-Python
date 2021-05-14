# 예제 7-3 Cython의 setup.py를 위해 이름만 변경한 순수 파이썬 코드

# cythonfn.pyx
def calculate_z(maxiter, zs, cs):
    """ 쥘리아 업데이트 규칙을 이용해 output 리스트를 계산한다. """
    output = [0] * len(zs)
    for i in range(len(zs)):
        n=0
        z = zs[i]
        c = cs[i]
        while n < maxiter and abs(z) < 2:
            z=z*z+c
            n += 1
        output[i] = n
    return output
