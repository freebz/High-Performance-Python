# 예제 6-5 순수 파이썬 2차원 확산 방정식 프로파일링

$ kernprof.py -lv diffusion_python.py
Wrote profile results to diffusion_python.py.lprof
Timer unit: 1e-06 s

Total time: 0 s
File: diffusion_python.py
Function: evolve at line 3

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     3                                           @profile
     4                                           def evolve(grid, dt, D=1.0):
     5                                               xmax, ymax = grid_shape
     6                                               new_grid = [[0.0,] * ymax for x in range(xmax)]
     7                                               for i in range(xmax):
     8                                                   for j in range(ymax):
     9                                                       grid_xx = grid[(i+1)%xmax][j] + grid[(i-1)%xmax][j] - 2.0 * grid[i][j]
    10                                                       grid_yy = grid[i][(j+1)%ymax] + grid[i][(j-1)%ymax] - 2.0 * grid[i][j]
    11                                                       new_grid[i][j] = grid[i][j] + D * (grid_xx + grid_yy) * dt
    12                                               return new_grid
