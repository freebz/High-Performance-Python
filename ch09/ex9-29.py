# 예제 9-29 multiprocessing을 사용해 numpy 배열을 공유하기 위한 worker_fn

def worker_fn(idx):
    # 다른 프로세스가 이미 이 값을 변경하지 않았는지 확인한다.
    assert main_nparray[idx, 0] == DEFAULT_VALUE
    # 하위 프로세스의 내부에서는 PID와 배열의 id를 출력해서
    # 복사본을 사용하는 것이 아님을 확인한다.
    if idx % 1000 == 0:
        print(" {}: with idx {}\n id of local_nparray_in_process is {} in PID {}"\
              .format(worker_fn.__name__, idx, id(main_nparray), os.getpid()))
    # 배열에 대해 어떤 작업이든 가능하다. 여기서는 대상 행의 모든 원소에
    # 프로세스의 PID 값을 저장한다.
    main_nparray[idx, :] = os.getpid()
