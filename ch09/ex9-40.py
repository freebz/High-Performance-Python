# 예제 9-40 락 없이 수를 세는 코드

import multiprocessing

def work(value, max_count):
    for n in range(max_count):
        value.value += 1

def run_workers():
...
    value = multiprocessing.Value('i', 0)
    for process_nbr in range(NBR_PROCESSES):
        p = multiprocessing.Process(target=work, args=(value, MAX_COUNT_PER_PROCESS))
        p.start()
        processes.append(p)
...
