# 예제 9-17 외부 레디스 서버를 사용해 플래그 공유하기

FLAG_NAME = b'redis_primes_flag'
FLAG_CLEAR = b'0'
FLAG_SET = b'1'

rds = redis.StrictRedis()

def check_prime_in_range((n, (from_i, to_i))):
    if n % 2 == 0:
        return False
    assert from_i % 2 != 0
    check_every = CHECK_EVERY
    for i in range(from_i, int(to_i), 2):
        check_every -= 1
        if not check_every:
            flag = rds[FLAG_NAME]
            if flag == FLAG_SET:
                return False
            check_every = CHECK_EVERY

        if n % i == 0:
            rds[FLAG_NAME] = FLAG_SET
            return False
    return True

def check_prime(n, pool, nbr_processes):
    # 가능성이 높은 인수를 큰 비용을 들이지 않고 검사한다.
    from_i = 3
    to_i = SERIAL_CHECK_CUTOFF
    rds[FLAG_SET] = FLAG_CLEAR
    if not check_prime_in_range((n, (from_i, to_i))):
        return False
    ...

    if False in results:
        return False
    return True
