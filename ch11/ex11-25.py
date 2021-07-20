# 예제 11-25 간단한 규모 가변성 블룸 필터 구현

from bloomfilter import BloomFilter

class ScalingBloomFilter(object):
    def __init__(self, capacity, error=0.005,
                 max_fill=0.8, error_tightening_raito=0.5):
        self.capacity = capacity
        self.base_error = error
        self.Max_fill = max_fill
        self.items_until_scale = int(capacity * max_fill)
        self.error_tightening_raito = error_tightening_raito
        self.bloom_filters = []
        self.current_bloom = None
        self._add_bloom()

    def _add_bloom(self):
        new_error = self.base_error * \
            self.error_tightening_raito ** len(self.bloom_filters)
        new_bloom = BloomFilter(self.capacity, new_error)
        self.bloom_filters.append(new_bloom)
        self.current_bloom = new_bloom
        return new_bloom

    def add(self, key):
        if key in self:
            return True
        self.current_bloom.add(key)
        self.items_until_scale -= 1
        if self.items_until_scale == 0:
            bloom_size = len(self.current_bloom)
            bloom_max_capacity = int(self.current_bloom.capacity * self.max_fill)

            # 블룸에 중복값을 많이 더했을 수도 있다. 따라서 실제로 크기를 키워야 할지
            # 아니면 아직 여유 공간이 있는지 검사할 필요가 있다.
            if bloom_size >= bloom_max_capacity:
                self._add_bloom()
                self.items_until_scale = bloom_max_capacity
            else:
                self.items_until_scale = int(bloom_max_capacity - bloom_size)
        return False

    def __contains__(self, key):
        return any(key in bloom for bloom in self.bloom_filters)

    def __len__(self):
        return sum(len(bloom) for bloom in self.bloom_filters)
