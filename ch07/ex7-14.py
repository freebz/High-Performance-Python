# 예제 7-14 @jit 데코레이터를 함수에 적용하기

from numba import jit
...
@jit()
def calculate_z_serial_purepython(maxiter, zs, cs, output):
