# 예제 7-1 쥘리아 함수에서 CPU를 많이 사용하는 코드

def calculate_z_serial_purepython(maxiter, zs, cs):
    """ 쥘리아 업데이트 규칙을 이용해 output 리스트를 계산한다. """
    output = [0] * len(zs)
    for i in range(len(zs)):
        n=0
        z = zs[i]
        c = cs[i]
        while n < maxiter and abs(z) < 2:
            z=z*z+c
            n += 1
        output[i] = n
    return output
