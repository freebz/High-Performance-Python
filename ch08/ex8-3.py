# 예제 8-3 순차적인 HTTP 크롤러

import requests
import string
import random

def generate_urls(base_url, num_urls):
    """
    URL의 맨 마지막에 임의의 문자를 추가해서 requests 라이브러리나
    서버의 캐시 기능을 무효화시킨다.
    """
    for i in range(num_urls):
        yield base_url + "".join(random.sample(string.ascii_lowercase, 10))

def run_experiment(base_url, num_iter=500):
    response_size = 0
    for url in generate_urls(base_url, num_iter):
        response = requests.get(url)
        response_size += len(response.text)
    return response_size

if __name__ == "__main__":
    import time
    delay = 100
    num_iter = 500
    base_url = "http://127.0.0.1:8080/add?name=serial&delay={}&".format(delay)

    start = time.time()
    result = run_experiment(base_url, num_iter)
    end = time.time()
    print("Result: {}, Time: {}".format(result, end - start))
