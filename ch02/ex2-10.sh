# 예제 2-10 calculate_z_serial_purepython에서 예상치 못한 메모리 사용을 보여주는 memory_profiler의 결과

$ python -m memory_profiler julia1_memoryprofiler.py
...
calculate_z_serial_purepythontook 17777.09674191475 seconds
Filename: julia1_memoryprofiler.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     9   36.332 MiB   36.332 MiB           1   @profile
    10                                         def calc_pure_python(desired_width, max_iterations):
    11                                             """복소 좌표(zs)와 복소 인자(cs) 리스트를 만들고,
    12                                             쥘리아 집합을 생성한 뒤 출력한다."""
    13   36.332 MiB    0.000 MiB           1       x_step = (float(x2 - x1) / float(desired_width))
    14   36.332 MiB    0.000 MiB           1       y_step = (float(y1 - y2) / float(desired_width))
    15   36.332 MiB    0.000 MiB           1       x = []
    16   36.332 MiB    0.000 MiB           1       y = []
    17   36.332 MiB    0.000 MiB           1       ycoord = y2
    18   36.332 MiB    0.000 MiB        1001       while ycoord > y1:
    19   36.332 MiB    0.000 MiB        1000           y.append(ycoord)
    20   36.332 MiB    0.000 MiB        1000           ycoord += y_step
    21   36.332 MiB    0.000 MiB           1       xcoord = x1
    22   36.332 MiB    0.000 MiB        1001       while xcoord < x2:
    23   36.332 MiB    0.000 MiB        1000           x.append(xcoord)
    24   36.332 MiB    0.000 MiB        1000           xcoord += x_step
    25                                             # 좌표 리스트와 각 셀에 g대ㅏㄴ 초기 조건을 만든다.
    26                                             # 초기 조건은 상수이며 쉽게 제거할 수 있는 점을 주목하자.
    27                                             # 우리가 만든 함수의 몇몇 입력을 사용한 실제 시나리오를 시뮬레이션할 때 사용한다.
    28   36.332 MiB    0.000 MiB           1       zs = []
    29   36.332 MiB    0.000 MiB           1       cs = []
    30  113.723 MiB   -1.781 MiB        1001       for ycoord in y:
    31  113.723 MiB -1799.742 MiB     1001000           for xcoord in x:
    32  113.723 MiB -1832.824 MiB     1000000               zs.append(complex(xcoord, ycoord))
    33  113.723 MiB -2260.746 MiB     1000000               cs.append(complex(c_real, c_imag))
    34                                         
    35  113.723 MiB    0.000 MiB           1       print("Length ox x:", len(x))
    36  113.723 MiB    0.000 MiB           1       print("Total elements:", len(zs))
    37  113.723 MiB    0.000 MiB           1       start_time = time.time()
    38  124.414 MiB  124.414 MiB           1       output = calculate_z_serial_purepython(max_iterations, zs, cs)
    39  124.414 MiB    0.000 MiB           1       end_time = time.time()
    40  124.414 MiB    0.000 MiB           1       secs = end_time - start_time
    41  124.414 MiB    0.000 MiB           1       print(calculate_z_serial_purepython.__name__ + "took", secs, "seconds")
    42                                         
    43                                             # 다음 sum은 1000^2 그리드에 300번의 반복을 가정한 값이다.
    44                                             # 제한된 입력으로 작업할 경우 발생할 수 있는 사소한 에러를 잡기 위한 목적이다.
    45  124.414 MiB    0.000 MiB           1       assert sum(output) == 33219980


Filename: julia1_memoryprofiler.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    48  113.723 MiB  113.723 MiB           1   @profile
    49                                         def calculate_z_serial_purepython(maxiter, zs, cs):
    50                                             """Calculate output list using Julia update rule"""
    51  121.199 MiB    7.477 MiB           1       output = [0] * len(zs)
    52  124.414 MiB    0.000 MiB     1000001       for i in range(len(zs)):
    53  124.414 MiB    0.000 MiB     1000000           n = 0
    54  124.414 MiB    0.000 MiB     1000000           z = zs[i]
    55  124.414 MiB    0.000 MiB     1000000           c = cs[i]
    56  124.414 MiB    3.215 MiB    34219980           while abs(z) < 2 and n < maxiter:
    57  124.414 MiB    0.000 MiB    33219980               z = z * z+ c
    58  124.414 MiB    0.000 MiB    33219980               n += 1
    59  124.414 MiB    0.000 MiB     1000000           output[i] = n
    60  124.414 MiB    0.000 MiB           1       return output
k
