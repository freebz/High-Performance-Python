# 예제 10-10 NSQ를 사용해 소수 계산을 분산 처리하기

import nsq
from tornado import partial
import ujson as json

@gen.coroutine
def write_message(topic, data, writer):
    response = yield gen.Task(writer.pub, topic, data)
    if isinstance(response, nsq.Error):
        print("Error with Message: {}: {}".format(data, response))
        yield write_message(data, writer)
    else:
        print("Published Message: ", data)

def calculate_prime(message, writer):
    message.enable_async()
    data = json.loads(message.body)
    prime = is_prime(data["number"])
    data["prime"] = prime
    if prime:
        topic = 'primes'
    else:
        topic = 'non_primes'

    output_message = json.dumps(data)
    write_message(topic, output_message, writer)
    message.finish()

if __name__ == "__main__":
    writer = nsq.Writer(['127.0.0.1:4150', ])
    handler = partial(calculate_prime, writer=writer)
    reader = nsq.Reader(
        message_handler = handler,
        nsqd_tcp_addresses = ['127.0.0.1:4150', ],
        topic = 'numbers',
        channel = 'worker_group_a',
    )
    nsq.run()
