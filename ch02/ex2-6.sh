# 예제 2-6 각 줄의 CPU 비용을 기록하기 위해 kernprof를 사용하여 프로파일링하기

$ kernprof.py -l -v julia1_lineprofiler.py
...
Wrote profile results to julia1_lineprofiler.py.lprof
Timer unit: 1e-06 s

Total time: 401.814 s
File: julia1_lineprofiler.py
Function: calculate_z_serial_purepython at line 47

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    47                                           @profile
    48                                           def calculate_z_serial_purepython(maxiter, zs, cs):
    49                                               """Calculate output list using Julia update rule"""
    50         1       8797.0   8797.0      0.0      output = [0] * len(zs)
    51   1000001    3424289.0      3.4      0.9      for i in range(len(zs)):
    52   1000000    3291797.0      3.3      0.8          n = 0
    53   1000000    3513028.0      3.5      0.9          z = zs[i]
    54   1000000    3436832.0      3.4      0.9          c = cs[i]
    55  34219980  143832088.0      4.2     35.8          while abs(z) < 2 and n < maxiter:
    56  33219980  124848109.0      3.8     31.1              z = z * z+ c
    57  33219980  115867907.0      3.5     28.8              n += 1
    58   1000000    3590920.0      3.6      0.9          output[i] = n
    59         1          3.0      3.0      0.0      return output
