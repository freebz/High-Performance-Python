# 예제 7-21 ctypes 2D 확산 코드

import ctypes

grid_shape = (512, 512)
_diffusion = ctypes.CDLL("../diffusion.so")

# 이후 작성할 코드를 단순하게 만들기 위해 C 타입에 대한 참조를 만든다.
TYPE_INT = ctypes.c_int
TYPE_DOUBLE = ctypes.c_double
TYPE_DOUBLE_SS = ctypes.POINTER(ctypes.POINTER(ctypes.c_double))

# evolve 함수의 시그니처를 다음과 같이 초기화한다.
# void evolve(int, int, double**, double**, double, double)
_diffusion.evolve.argtypes = [
    TYPE_INT,
    TYPE_INT,
    TYPE_DOUBLE_SS,
    TYPE_DOUBLE_SS,
    TYPE_DOUBLE,
    TYPE_DOUBLE,
]
_diffusion.evolve.restype = None

def evolve(grid, out, dt, D=1.0):
    # 우선 파이썬 타입을 그에 맞는 C 타입으로 변환한다.
    cX = TYPE_INT(grid_shape[0])
    cY = TYPE_INT(grid_shape[1])
    cdt = TYPE_DOUBLE(dt)
    cD = TYPE_DOUBLE(D)
    pointer_grid = grid.ctypes.data_as(TYPE_DOUBLE_SS)
    pointer_out = out.ctypes.data_as(TYPE_DOUBLE_SS)

    # 이제 C 언어 evolve 함수를 호출할 수 있다.
    _diffusion.evolve(cX, cY, pointer_grid, pointer_out, cD, cdt)
