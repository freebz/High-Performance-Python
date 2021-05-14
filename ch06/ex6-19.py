# 예제 6-19 numexpr을 사용해서 대규모 행렬 연산을 최적화하기

from numexpr import evaluate

def evolve(grid, dt, next_grid, D=1):
    laplacian(grid, next_grid)
    evaluate("next_grid*D*dt*grid", out=next_grid)
