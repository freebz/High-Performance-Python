# 예제 8-5 grequests HTTP 크롤러

import grequests

def run_experiment(base_url, num_iter=500):
    urls = generate_urls(base_url, num_iter)
    response_futures = (grequests.get(u) for u in urls)
    response = grequests.imap(response_futures, size = 100)
    response_size = sum(len(r.text) for r in responses)
    return response_size
