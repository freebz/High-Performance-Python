# 예제 9-16 Manager.Value 객체를 플래그로 넘기기

def check_prime_in_range((n, (from_i, to_i), value)):
    if n % 2 == 0:
        return False
    assert from_i % 2 != 0
    check_every = CHECK_EVERY
    for i in range(from_i, int(to_i), 2):
        check_every -= 1
        if not check_every:
            if value.value == FLAG_SET:
                return False
            check_every = CHECK_EVERY
        if n % i == 0:
            value.value = FLAG_SET
            return False
    return True
        
