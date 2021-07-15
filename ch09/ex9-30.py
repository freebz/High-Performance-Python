# 예제 9-30 numpy 배열을 공유하도록 설정하는 main

if __name__ == '__main__':
    DEFAULT_VALUE = 42
    NBR_OF_PROCESSES = 4

    # 바이트들로 이뤄진 블록을 만들고 이를 로컬 numpy 배열로 reshape한다.
    NBR_ITEMS_IN_ARRAY = SIZE_A * SIZE_B
    shared_array_base = multiprocessing.Array(ctypes.c_double,
                                              NBR_ITEMS_IN_ARRAY, lock=False)
    main_nparray = np.frombuffer(shared_array_base, dtype=ctypes.c_double)
    main_nparray = main_nparray.reshape(SIZE_A, SIZE_B)
    # 복사가 이뤄지지 않았음을 확인한다.
    assert main_nparray.base.base is shared_array_base
    print("Created shared array with {:,} nbytes".format(main_nparray.nbytes))
    print("Shared array id is {} in PID {}".format(id(main_nparray), os.getpid()))
    print("Starting with an array of 0 values:")
    print(main_nparray)
    print()
