# 예제 8-7 콜백을 사용하는 tornado 크롤러

from tornado import ioloop
from tornado.httpclient import AsyncHTTPClient

from functools import partial

AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient",
                          max_clients=100)

def fetch_urls(urls, callback):
    http_client = AsyncHTTPClient()
    urls = list(urls)
    response = []
    def _finish_fetch_urls(result):
        responses.append(result)
        if len(responses) == len(urls):
            callback(responses)
    for url in urls:
        http_client.fetch(url, callback=_finish_fetch_urls)

def run_experiment(base_url, num_iter=500, callback=None):
    urls = generate_urls(base_url, num_iter)
    callback_passthrou = partial(_finish_run_experiment,
                                 callback=callback)
    fetch_urls(urls, callback_passthrou)

def _finish_run_experiment(responses, callback):
    response_sum = sum(len(r.body) for r in responses)
    print(response_sum)
    callback()

if __name__ == "__main__":
    # ...초기화...

    _ioloop = ioloop.IOLoop.instance()
    _ioloop.add_callback(run_experiment, base_url, num_iter, _ioloop.stop)

    _ioloop.start()
