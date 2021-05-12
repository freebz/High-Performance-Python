# 예제 2-7 각각의 소요 시간을 측정하기 위해 합쳐져 있던 while문을 나눈 코드

$ kernprof.py -l -v julia1_lineprofiler2.py
...
Wrote profile results to julia1_lineprofiler2.py.lprof
Timer unit: 1e-06 s

Total time: 639.285 s
File: julia1_lineprofiler2.py
Function: calculate_z_serial_purepython at line 47

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    47                                           @profile
    48                                           def calculate_z_serial_purepython(maxiter, zs, cs):
    49                                               """Calculate output list using Julia update rule"""
    50         1       8962.0   8962.0      0.0      output = [0] * len(zs)
    51   1000001    3490003.0      3.5      0.5      for i in range(len(zs)):
    52   1000000    3384616.0      3.4      0.5          n = 0
    53   1000000    3640982.0      3.6      0.6          z = zs[i]
    54   1000000    3518448.0      3.5      0.6          c = cs[i]
    55                                                   while True:
    56  34219980  141122531.0      4.1     22.1              not_yet_escaped = abs(z) < 2
    57  34219980  121204957.0      3.5     19.0              iterations_left = n < maxiter
    58  34219980  116782931.0      3.4     18.3              if not_yet_escaped and iterations_left:
    59  33219980  124106490.0      3.7     19.4                  z = z * z + c
    60  33219980  118437811.0      3.6     18.5                  n += 1
    61                                                       else:
    62                                                           break
    63   1000000    3587682.0      3.6      0.6          output[i] = n
    64         1          4.0      4.0      0.0      return output
