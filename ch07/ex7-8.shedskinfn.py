# 예제 7-8 CPU 위주의 함수를 별도의 모듈로 분리해서(Cython에서와 마찬가지) Shed Skin이 자동으로 타입을 추론 할 수 있게 만들기

# shedskinfn.py
def calculate_z(maxiter, zs, cs):
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

if __name__ == "__main__":
    # 올바른 타입의 전형적인 예를 사용해서 타입을 추론할 수 있게 만든다.
    # 함수를 호출해서 Shed Skin이 타입을 분석하게 만든다
    output = calculate_z(1, [0j], [0j])
