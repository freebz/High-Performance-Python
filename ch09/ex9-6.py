# 예제 9-6 IPC를 위한 두 개의 대기열 만들기

if __name__ == "__main__":
    primes = []

    manager = multiprocessing.Manager()
    possible_primes_queue = manager.Queue()
    definite_primes_queue = manager.Queue()

    NBR_PROCESSES = 2
    pool = Pool(processes=NBR_PROCESSES)
    processes = []
    for _ in range(NBR_PROCESSES):
        p = multiprocessing.Process(target=check_prime,
                                    args=(possible_primes_queue,
                                          definite_primes_queue))
        processes.append(p)
        p.start()

    t1 = time.time()
    number_range = range(100000000, 10100000)

    # 전달되는 작업 대기열에 작업을 추가한다.
    for possible_prime in number_range:
        possible_primes_queue.put(possible_prime)

    # 원격 작업자를 중단시키기 위해 포이즌 필을 추가한다.
    for n in range(NBR_PROCESSES):
        possible_primes_queue.put(FLAG_ALL_DONE)
