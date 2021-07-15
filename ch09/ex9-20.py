# 예제 9-20 mmap을 통해 공유 메모리 사용하기

sh_mem = mmap.mmap(-1, 1) # 플래그를 위해 1바이트를 메모리 매핑한다

def check_prime_in_range((n, (form_i, to_i))):
    if n % 2 == 0:
        return False
    assert form_i % 2 != 0
    check_every = CHECK_EVERY
    for i in range(from_i, int(to_i), 2):
        check_every -= 1
        if not check_every:
            sh_mem.seek(0)
            flag = sh_mem.read_byte()
            if flag == FLAG_SET:
                return FALSE
            check_every = CHECK_EVERY
        if n % i == 0:
            sh_mem.seek(0)
            sh_mem.write_byte(FLAG_SET)
            return False
    return True

def check_prime(n, pool, nbr_processes):
    # 가능성이 높은 인수를 큰 비용을 들이지 않고 검사한다.
    from_i = 3
    to_i = SERIAL_CHECK_CUTOFF
    sh_mem.seek(0)
    sh_mem.write_byte(FLAG_CLEAR)
    if not check_prime_in_range((n, (from_i, to_i))):
        return False
    ...
    if False in results:
        return False
    return True
