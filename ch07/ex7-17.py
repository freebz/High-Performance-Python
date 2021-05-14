# 예제 7-17 Pythran이 OpenMP를 지원하도록 calculate_z에 애너테이션 달기

#pythran export calculate_z(int, complex[], complex[], int[])
def calculate_z(maxiter, zs, cs, output):
    #omp parallel for schedule(guided)
    for i in range(len(zs)):
