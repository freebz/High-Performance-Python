# 예제 4-6 두 소문자를 조합한 최적 해시 함수

def twoletter_hash(key):
    offset = ord('a')
    k1, k2 = key
    return (ord(k2) - offset) + 26 * (ord(k1) - offset)
