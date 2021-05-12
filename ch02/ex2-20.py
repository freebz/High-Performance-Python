# 예제 2-20 @profile을 사용할 간단한 함수와 테스트

# ex.py
import unittest

@profile
def some_fn(nbr):
    return nbr * 2

class TestCase(unittest.TestCase):
    def test(self):
        result = some_fn(2)
        self.assertEquals(result, 4)
