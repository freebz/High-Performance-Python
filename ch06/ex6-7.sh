# 예제 6-7 메모리 할당을 줄인 파이썬 확산 방정식 코드의 프로파일링 결과

$ kernprof.py -lv diffusion_python_memory.py
Wrote profile results to diffusion_python_memory.py.lprof
Timer unit: 1e-06 s

Total time: 0 s
File: diffusion_python_memory.py
Function: evolve at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           @profile
     2                                           def evolve(grid, dt, out, D=1.0):
     3                                               xmax, ymax = grid_shape
     4                                               for i in range(xmax):
     5                                                   for j in range(ymax):
     6                                                       grid_xx = grid[(i+1)%xmax][j] + grid[(i-1)%xmax][j] - 2.0 * grid[i][j]
     7                                                       grid_yy = grid[i][(j+1)%ymax] + grid[i][(j-1)%ymax] - 2.0 * grid[i][j]
     8                                                       out[i][j] = grid[i][j] + D * (grid_xx + grid_yy) * dt
