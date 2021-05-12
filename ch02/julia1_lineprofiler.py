"""PIL 기반의 이미지 생성을 제외한 쥘리아 집합 생성기"""
import time

# 계산할 복소평면 영역
x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -.42193


def calc_pure_python(desired_width, max_iterations):
    """복소 좌표(zs)와 복소 인자(cs) 리스트를 만들고,
    쥘리아 집합을 생성한 뒤 출력한다."""
    x_step = (float(x2 - x1) / float(desired_width))
    y_step = (float(y1 - y2) / float(desired_width))
    x = []
    y = []
    ycoord = y2
    while ycoord > y1:
        y.append(ycoord)
        ycoord += y_step
    xcoord = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step
    # 좌표 리스트와 각 셀에 g대ㅏㄴ 초기 조건을 만든다.
    # 초기 조건은 상수이며 쉽게 제거할 수 있는 점을 주목하자.
    # 우리가 만든 함수의 몇몇 입력을 사용한 실제 시나리오를 시뮬레이션할 때 사용한다.
    zs = []
    cs = []
    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))

    print("Length ox x:", len(x))
    print("Total elements:", len(zs))
    start_time = time.time()
    output = calculate_z_serial_purepython(max_iterations, zs, cs)
    end_time = time.time()
    secs = end_time - start_time
    print(calculate_z_serial_purepython.__name__ + "took", secs, "seconds")

    # 다음 sum은 1000^2 그리드에 300번의 반복을 가정한 값이다.
    # 제한된 입력으로 작업할 경우 발생할 수 있는 사소한 에러를 잡기 위한 목적이다.
    assert sum(output) == 33219980


@profile
def calculate_z_serial_purepython(maxiter, zs, cs):
    """Calculate output list using Julia update rule"""
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


if __name__ == "__main__":
    # 노트북에 적절한 기본값으로 쥘리아 집합을 구하는 순수 파이썬 구현
    calc_pure_python(desired_width=1000, max_iterations=300)
