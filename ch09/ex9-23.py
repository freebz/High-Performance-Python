# 예제 9-23 속도 향상을 추가로 얻기 위해서 "팀의 개발 속도에 해를 끼치지 말라"는 규칙을 깬 코드

def check_prime_in_range((n, (from_i, to_i))):
    if n % 2 == 0:
        return False
    assert from_i % 2 != 0
    FLAG_SET_LOCAL = FLAG_SET
    sh_seek = sh_mem.seek
    sh_read_byte = sh_mem.read_byte
    for outer_counter in range(from_i, int(to_i), CHECK_EVERY):
        upper_bound = min(int(to_i), outer_counter + CHECK_EVERY)
        for i in range(outer_counter, upper_bound, 2):
            if n % i == 0:
                sh_seek(0)
                sh_mem.write_byte(FLAG_SET)
                return False
        sh_seek(0)
        if sh_read_byte() == FLAG_SET_LOCAL:
            return False
    return True
