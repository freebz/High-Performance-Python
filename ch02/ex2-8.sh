# 예제 2-8 while문의 조건 감사 순서를 바꿔 실행 속도를 약간 개선함

$ kernprof.py -l -v julia1_lineprofiler3.py
...
Wrote profile results to julia1_lineprofiler3.py.lprof
Timer unit: 1e-06 s

Total time: 393.179 s
File: julia1_lineprofiler3.py
Function: calculate_z_serial_purepython at line 47

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    47                                           @profile
    48                                           def calculate_z_serial_purepython(maxiter, zs, cs):
    49                                               """Calculate output list using Julia update rule"""
    50         1       8670.0   8670.0      0.0      output = [0] * len(zs)
    51   1000001    3379941.0      3.4      0.9      for i in range(len(zs)):
    52   1000000    3267117.0      3.3      0.8          n = 0
    53   1000000    3531384.0      3.5      0.9          z = zs[i]
    54   1000000    3384799.0      3.4      0.9          c = cs[i]
    55  34219980  140444941.0      4.1     35.7          while n < maxiter and abs(z) < 2:
    56  33219980  121337247.0      3.7     30.9              z = z * z + c
    57  33219980  114331108.0      3.4     29.1              n += 1
    58   1000000    3493940.0      3.5      0.9          output[i] = n
    59         1          4.0      4.0      0.0      return output
