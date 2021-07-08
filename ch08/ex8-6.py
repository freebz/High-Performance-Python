# 예제 8-6 tornado를 활용한 HTTP 크롤러

from tornado import ioloop
from tornado.httpclient import AsyncHTTPClient
from tornado import gen

from functools import partial
import string
import random

AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient",
                          max_clients=100)

def generate_urls(base_url, num_urls):
    for i in range(num_urls):
        yield base_url + "".join(random.sample(string.ascii_lowercase, 10))

@gen.coroutine
def run_experiment(base_url, num_iter=500):
    http_client = AsyncHTTPClient()
    urls = generate_urls(base_url, num_iter)
    responses = yield [http_client.fetch(url) for url in urls]
    response_sum = sum(len(r.body) for r in responses)
    raise gen.Return(value=response_sum)

if __name__ == "__main__":
    #...초기화...

    _ioloop = ioloop.IOLoop.instance()
    run_func = partial(run_experiment, base_url, num_iter)
    result = _ioloop.run_sync(run_func)
