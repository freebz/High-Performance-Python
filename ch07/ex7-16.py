# 예제 7-16 evolve()의 진입점을 지정하기 위한 애너테이션 주석을 한 줄 추가한다.

import numpy as np
def laplacian(grid):
    return np.roll(grid, +1, 0) +
                   np.roll(grid, -1 , 0) +
                   np.roll(grid, +1, 1) +
                   np.roll(grid, -1, 1) - 4 * grid

#pythran export evolve(float64[][], float)
def evolve(grid, dt, D=1):
    return grid + dt * D * laplacian(grid)
