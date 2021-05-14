# 예제 7-10 Shed Skin이 추론한 타입을 분석하기 위해 타입 애너테이션이 달린 출력을 분석하기

# shedskinfn.ss.py
def calculate_z(maxiter, zs, cs):                   # maxiter: [int],
                                                    # zs: [list(complex)],
                                                    # cs: [list(complex)]
    """ 쥘리아 업데이트 규칙을 이용해 output 리스트를 계산한다. """
    output = [0] * len(zs)                          # [list(int)]
    for i in range(len(zs)):                        # [__iter(int)]
        n=0                                         # [int]
        z = zs[i]                                   # [complex]
        c = cs[i]                                   # [complex]
        while n < maxiter and abs(z) < 2:           # [complex]
            z=z*z+c                                 # [complex]
            n += 1                                  # [complex]
        output[i] = n                               # [int]
    return output                                   # [list(int)]

if __name__ == "__main__":                          # [] 
    # 올바른 타입의 전형적인 예를 사용해서 타입을 추론할 수 있게 만든다.
    # 함수를 호출해서 Shed Skin이 타입을 분석하게 만든다
    output = calculate_z(1, [0j], [0j])             # [list(int)] 
