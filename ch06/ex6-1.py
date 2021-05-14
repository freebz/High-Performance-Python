# 예제 6-1 단순(1차원) 확산 의사 코드

# 초기 조건을 생성한다.
u = vector of length N
for i in range(N):
    u = 0 if there is water, 1 if there is dye

# 초기 조건을 변경한다.
D = 1
t = 0
dt = 0.0001
while True:
    print("Current time is: %f" % t)
    unew = vector of size N
    # 행렬의 각 셀을 갱신한다.
    for i in range(N):
        unew[i] = u[i] + D * dt * (u[(i+1)%N] + u[(i-1)%N] - 2 * u[i])
    # 갱신된 해법을 u로 옮긴다.
    u = unew

    visualize(u)
