# 예제 2-17 같은 문제를 해결하는 효율적인 방법과 그렇지 않은 방법

def fn_expressive(upper = 1000000):
    total = 0
    for n in range(upper):
        total += n
    return total

def fn_terse(upper = 1000000):
    return sum(range(upper))

print("Functions return the same result:", fn_expressive() == fn_terse())
# Functions return the same result: True
