# 예제 6-21 scipy의 laplace 필터를 사용한 예

from scipy.ndimage.filters import laplace

def laplacian(grid, out):
    laplace(grid, out, mode='wrap')
