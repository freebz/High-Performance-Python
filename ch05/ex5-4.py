# 예제 5-4 제너레이터 기반의 특이점 찾기

import math

def check_anomaly((day, day_data)):
    # 해당 날짜의 평균, 표준편차, 최댓값을 구한다.
    # 해당 날짜의 데이터를 한 번만 읽어서 계산할 수 있도록
    # 단일 패스 평균/표준편차 알고리즘을 사용한다.
    n = 0
    mean = 0
    M2 = 0
    max_value = None

    for timestamp, value in day_data:
        n += 1
        delta = value - mean
        mean = mean + delta/n
        M2 += delta*(value - mean)
        if max_value:
            max_value = max(max_value, value)
        else:
            max_value = value
    variance = M2/(n - 1)
    standard_deviation = math.sqrt(variance)

    # 다음은 실제로 해당 날짜의 데이터가 특이점이라면 해당 날짜를 반환하고
    # 그렇지 않다면 False 반환한다.
    if max_value > mean + 3 * standard_deviation:
        return day
    return False
