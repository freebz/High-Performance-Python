# 예제 9-8 비동기적으로 작업을 제공하는 함수

def feed_new_jobs(number_range, possible_primes_queue, nbr_poison_fills):
    for possible_prime in number_range:
        possible_primes_queue.put(possible_prime)
    # 원격 프로세스를 종료시키기 위해 포이즌 필을 추가한다.
    for n in range(nbr_poison_fills):
        possible_primes_queue.put(FLAG_ALL_DONE)
