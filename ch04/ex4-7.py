# 예제 2-7 좋은 해시 함수와 나쁜 해시 함수의 시간 차이

import string
import timeit

class BadHash(str):
    def __hash__(self):
        return 42

class GoodHash(str):
    def __hash__(self):
        """
        아래는 twoletter_hash 함수를 약간 개선한 버전이다.
        """
        return ord(self[1]) + 26 * ord(self[0]) - 2619

baddict = set()
gooddict = set()
for i in string.ascii_lowercase:
    for j in string.ascii_lowercase:
        key = i + j
        baddict.add(BadHash(key))
        gooddict.add(GoodHash(key))

badtime = timeit.repeat(
    "key in baddict",
    setup = "from __main__ import baddict, BadHash; key = BadHash('zz')",
    repeat = 3,
    number = 1000000,
)
goodtime = timeit.repeat(
    "key in gooddict",
    setup = "from __main__ import gooddict, GoodHash; key = GoodHash('zz')",
    repeat = 3,
    number = 1000000,
)

print("Min lookup time for baddict: ", min(badtime))
print("Min lookup time for gooddict: ", min(goodtime))

# 결과
# 나쁜 사전(baddict)의 최단 탐색 시간: 16.3375990391
# 좋은 사전(gooddict)의 최단 탐색 시간: 0.748275995255

# Min lookup time for baddict:  40.07257298287004
# Min lookup time for gooddict:  0.5619166211690754
