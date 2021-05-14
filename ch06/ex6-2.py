# 예제 6-2 2차원 확산을 계산하는 알고리즘

for i in range(N):
    for j in range(N):
        unew[i][j] = u[i][j] + dt * (                       \
            (u[(i+1)%N][j] + u[(i-1)%N][j] - 2 * u[i][j]) + \ # d^2 u / dx^2
            (u[i][(j+1)%M] + u[j][(j-1)%M] - 2 * u[i][j])   \ # d^2 u / dy^2
        )
