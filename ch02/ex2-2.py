# 예제 2-2 계산 함수에 입력으로 넘길 좌표 리스트 생성

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
