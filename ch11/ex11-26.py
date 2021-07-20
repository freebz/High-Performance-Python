# 예제 11-26 간단히 구현한 로그로그 레지스터

import mmh3

def trailing_zeros(number):
    """
    오른쪽 끝부터 시작하며, 32비트 정수에서 가장 처음 1로 설정된 비트의 색인을 반환한다.

    >>> trailing_zeros(0)
    32
    >>> trailing_zeros(0b1000)
    3
    >>> trailing_zeros(0b10000000)
    7
    """
    if not number:
        return 32
    index = 0
    while (number >> index) & 1 == 0:
        index += 1
    return index

class LogLogRegister(object):
    counter = 0

    def add(self, item):
        item_hash = mmh3.hash(str(item))
        return self._add(item_hash)

    def _add(self, item_hash):
        bit_index = trailing_zeros(item_hash)
        if bit_index > self.counter:
            self.counter = bit_index

    def __len__(self):
        return 2**self.counter
