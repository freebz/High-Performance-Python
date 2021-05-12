# 예제 3-2 리스트의 선형 탐색

def linear_search(needle, array):
    for i, item in enumerate(array):
        if item == needle:
            return i
    return -1
