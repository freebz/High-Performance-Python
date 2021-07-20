# 예제 11-9 bisect를 사용하기 위한 준비인 sort 연산에 걸리는 시간 재기

t1 = time.time()
words = [w for w in text_example.readers]
print("Loading {} words".format(len(words)))
t2 = time.time()
print("RAM after creating list {:0.1f}MiB, took {:0.1f}s".
      format(memory_profiler.memory_usage()[0], t2 - t1))
print("The list contains {} words".format(len(words)))
words.sort()
t3 = time.time()
print("Sroting list took {:0.1f}s".format(t3 - t2))
