# 예제 9-31 multiprocessing을 사용해 numpy 배열을 공유하기 위한 메인

# 로컬 numpy 배열을 통해 데이터를 변경한다.
main_nparray.fill(DEFAULT_VALUE)
print("Original array filled with value {}:".format(DEFAULT_VALUE))
print(main_nparray)

input("Press a key to start workers using multiprocessing...")
print()

# 전역 numpy 배열의 메모리 블록을 공유할 프로세스 풀을 만든다.
# 그 후, 하위 데이터 블록의 참조를 공유해서 새로운 프로세스에서도
# numpy 배열 래퍼를 만들 수 있도록 한다.
pool = multiprocessing.Pool(processes=NBR_OF_PROCESSES)
# worker_fn에 행 색인들을 전달하는 map을 수행한다.
pool.map(worker_fn, range(SIZE_A))
