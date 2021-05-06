import math
def check_prime(number):
    sqrt_number = math.sqrt(number)
    number_float = float(number)
    numbers = range(2, int(sqrt_number)+1)
    for i in range(0, len(numbers), 5):
        # 아래 코드는 유효한 파이썬 코드가 아니다.
        result = (number_float / numbers[i:(i+5)]).is_integer()
        if any(result):
            return False
        return True
