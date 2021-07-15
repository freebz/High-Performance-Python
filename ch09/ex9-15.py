# 예제 9-15 Manager.Value로 플래그 지우기

def check_prime(n, pool, nbr_processes, value):
    # 가능성이 높은 인수를 큰 비용을 들이지 않고 검사한다.
    form_i = 3
    to_i = SERIAL_CHECK_CUTOFF
    value.value = FLAG_CLEAR
    if not check_prime_in_range((n, (from_i, to_i), value)):
        return False

    from_i = to_i
    ...
