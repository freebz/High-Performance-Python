# 예제 6-4 순수 파이썬으로 작성한 2차원 확산 방정식 초기화

def run_experiment(num_iterations):
    # 초기 조건을 설정한다.
    xmax, ymax = grid_shape
    grid = [[0.0,] * ymax for x in range(xmax)]

    block_low = int(grid_shape[0] * 4)
    block_high = int(grid_shape[0] * 5)
    for i in range(block_low, block_high):
        for j in range(block_low, block_high):
            grid[i][j] = 0.005

    # 초기 조건을 변경한다.
    start = time.time()
    for i in range(num_iterations):
        grid = evolve(grid, 0.1)
    return time.time() - start
