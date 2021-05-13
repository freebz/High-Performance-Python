# 예제 4-9 네임스페이스 탐색 과정의 역어셈블

dis.dis(test1)
#  11           0 LOAD_GLOBAL              0 (math)  # 사전 탐색
#               2 LOAD_METHOD              1 (sin)   # 사전 탐색
#               4 LOAD_FAST                0 (x)     # 지역 변수 탐색
#               6 CALL_METHOD              1
#               8 RETURN_VALUE

dis.dis(test2)
#  18           0 LOAD_GLOBAL              0 (sin)   # 사전 탐색
#               2 LOAD_FAST                0 (x)     # 지역 변수 탐색
#               4 CALL_FUNCTION            1
#               6 RETURN_VALUE

dis.dis(test3)
#  25           0 LOAD_FAST                1 (sin)   # 지역 변수 탐색
#               2 LOAD_FAST                0 (x)     # 지역 변수 탐색
#               4 CALL_FUNCTION            1
#               6 RETURN_VALUE
