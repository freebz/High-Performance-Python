# 예제 9-7 대기열 두 개를 사용해 IPC하기

processors_indicating_they_have_finished = 0
while True:
    new_result = definite_primes_queue.get() # 결과를 기다리면서 블록된다.
    if new_result == FLAG_WORKER_FINISHED_PROCESSING:
        processors_indicating_they_have_finished += 1
        if processors_indicating_they_finished == NBR_PROCESSES:
            break
    else:
        primes.append(new_result)
assert processors_indicating_they_finished == NBR_PROCESSES

print("Took:", time.time() - t1)
print(len(primes), primes[:10], primes[-10:])
