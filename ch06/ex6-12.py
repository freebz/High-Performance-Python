# 예제 6-12 메모리 할당을 줄이기 위한 제자리 연산

import numpy as np
array1 = np.random.random((10,10))
array2 = np.random.random((10,10))
id(array1)
# 140062009933136
array1 += array2
id(array1)
# 140062009933136
