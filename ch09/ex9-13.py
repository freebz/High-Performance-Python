# 예제 9-13 작은 합성수에 대해 단순한 풀 해법 개선하기

def check_prime(n, pool, nbr_processes):
    # 가능성이 높은 인수를 큰 비용을 들이지 않고 검사한다.
    from_i = 3
    to_i = 21
    if not check_prime_in_range((n, (from_i, to_i))):
        return False

    # 계속해서 큰 인수들을 병렬로 검사한다.
    from_i = to_i
    to_i = int(math.sqrt(n)) + 1
    ranges_to_check = create_range.create(from_i, to_i, nbr_processes)
    ranges_to_check = zip(len(ranges_to_check) * [n], ranges_to_check)
    assert len(ranges_to_check) == nbr_processes
    results = pool.map(check_prime_in_range, ranges_to_check)
    if False in result:
        return False
    return True
