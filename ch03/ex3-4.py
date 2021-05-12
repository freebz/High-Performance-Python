# 예제 3-4 bisect 모듈을 이용해서 가까운 값 찾기

import bisect
import random

def find_closest(haystack, needle):
    # bisect.bisect_left는 haystack에서 needle보다 크거나 같은
    # 첫 번째 값의 위치를 반환한다.
    i = bisect.bisect_left(haystack, needle)
    if i == len(haystack):
        return i - 1
    elif haystack[i] == needle:
        return i
    elif i > 0:
        j = i - 1
        # 여기서, i번째 값은 needle보다 크므로(반대로 j번째 값은 needle보다 적다)
        # i번째 값과 j번째 값 중 어떤 값이 needle에 가까운지 비교하기 위해
        # 절대값을 사용할 필요가 없다.
        if haystack[i] - needle > needle - haystack[j]:
            return j
    return i

important_numbers = []
for i in range(10):
    new_number = random.randint(0, 1000)
    bisect.insort(important_numbers, new_number)

# bisect.insort로 추가했기 때문에 important_numbers는 정렬된 상태로 추가되었다.
print("Haystack: ", important_numbers)

closest_index = find_closest(important_numbers, -250)
print("Closest value to -250: ", important_numbers[closest_index])

closest_index = find_closest(important_numbers, 500)
print("Closest value to 500: ", important_numbers[closest_index])

closest_index = find_closest(important_numbers, 1100)
print("Closest value to 1100: ", important_numbers[closest_index])
