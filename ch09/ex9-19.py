# 예제 9-19 RawValue를 만들어서 전달하기

if __name__ == "__main__":
    NBR_PROCESSES = 4
    value = multiprocessing.RawValue(b'c', FLAG_CLEAR) # 1 바이트 문자
    pool = Pool(processes=NBR_PROCESSES)
    ...
