# 예제 9-28 multiprocessing을 사용해 numpy 배열 공유하기

import os
import multiprocessing
from collections import Counter
import ctypes
import numpy as np
from prettytable import PrettyTable

SIZE_A, SIZE_B = 10000, 80000  # 6.2GB - 스왑을 사용하기 시작함(메모리를 최대로 사용함)
