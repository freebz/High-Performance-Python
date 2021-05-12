# 예제 2-13 코드 실행 각 단계별로 얼마나 많은 객체가 생성되었는지를 보여주는 heapy의 결과

$ python julia1_guppy.py
heapy after creating y and x lists of floats
Partition of a set of 27293 objects. Total size = 3416032 bytes.
 Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
     0  10960  40  1050376  31    1050376  31 str
     1   5768  21   465016  14    1515392  44 tuple
     2    199   1   210856   6    1726248  51 dict of type
     3     72   0   206784   6    1933032  57 dict of module
     4   1592   6   203776   6    2136808  63 types.CodeType
     5    313   1   201304   6    2338112  68 dict (no owner)
     6   1557   6   186840   5    2524952  74 function
     7    199   1   177008   5    2701960  79 type
     8    124   0   135328   4    2837288  83 dict of class
     9   1045   4    83600   2    2920888  86 __builtin__.wrapper_descriptor
<91 more rows. Type e.g. '_.more' to view.>

heapy after creating za and cs using complex numbers
Partition of a set of 2027301 objects. Total size = 83671256 bytes.
 Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
     0 2000000  99 64000000  76  64000000  76 complex
     1    185   0 16295368  19  80295368  96 list
     2  10962   1  1050504   1  81345872  97 str
     3   5767   0   464952   1  81810824  98 tuple
     4    199   0   210856   0  82021680  98 dict of type
     5     72   0   202984   0  82635224  99 dict of module
     6   1592   0   203776   0  82432240  99 types.CodeType
     7    319   0   202984   0  82635224  99 dict (no owner)
     8   1556   0   186720   0  82821944  99 function
     9    199   0   177008   0  82998952  99 type
<92 more rows. Type e.g. '_more' to view.>

Length of x: 1000
Total elements: 1000000
calculate_z_serial_purepython took 13.2436609268 seconds

heapy after calling calculate_z_serial_purepython
Partition of a set of 2127696 objects. Total size = 94207376 bytes.
 Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
     0 2000000  94 64000000  68  64000000  68 complex
     1    186   0 24421904  26  88421904  94 list
     2 100965   5  2423160   3  90845064  96 int
     3  10962   1  1050504   1  91895568  98 str
     4   5767   0   464952   0  92360520  98 tuple
     5    199   0   210856   0  92571376  98 dict of type
     6     72   0   206784   0  92778160  98 dict of module
     7   1592   0   203776   0  92981936  99 types.CodeType
     8    319   0   202984   0  93184920  99 dict (no owner)
     9   1556   0   186720   0  93371640  99 function
<92 more rows. Type e.g. '_.more' to view.>
