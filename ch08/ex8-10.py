import grequests

class AsyncBatcher(object):
    __slots__ = ["batch", "batch_size", "save", "flush"]
    def __init__(self, batch_size):
        self.batch_size = batch_size
        self.batch = []

    def save(self, prime):
        url = "http://127.0.0.1:8080/add?prime={}".format(prime)
        self.batch.append((url,prime))
        if len(self.batch) == self.batch_size:
            self.flush()

    def flush(self):
        responses_futures = (grequests.get(url) for url, _ in self.batch)
        responses = grequests.map(responses_futures)
        for response, (url, prime) in zip(responses, self.batch):
            finish_save_prime(response, prime)
        self.batch = []


def calculate_primes_async(max_number):
    batcher = AsyncBatcher(100)
    for number in range(max_number):
        if check_prime(number):
            batcher.save(number)
    batcher.flush()
    return
