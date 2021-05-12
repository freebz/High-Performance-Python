# 예제 2-3 CPU를 집중적으로 사용하는 계산 함수

def calculate_z_serial_purepython(maxiter, zs, cs):
    """쥘리아 갱신 규칙을 사용해서 output 리스트 계산하기"""
    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        while abs(z) < 2 and n < maxiter:
            z = z * z+ c
            n += 1
        output[i] = n
    return output
