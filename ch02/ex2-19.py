# 예제 2-19 dis 모듈을 사용해서 두 함수의 바이트코드 명령어 개수 확인하기

import dis
print fn_expressive.func_name
dis.dis(fn_expressive)

fn_expressive
  2            0 LOAD_CONST               1 (0)
               3 STORE_FAST               1 (total)

  3            6 SETUP_LOOP              30 (to 39)
               9 LOAD_GLOBAL              0 (range)
              12 LOAD_FAST                0 (upper)
              15 CALL_FUNCTION            1
              18 GET_ITER
         >>   19 FOR_ITER                16 (to 38)
              22 STORE_FAST               2 (n)

  4           25 LOAD_FAST                1 (total)
              28 LOAD_FAST                2 (n)
              31 INPLACE_ADD
              32 STORE_FAST               1 (total)
              35 JUMP_ABSOLUTE           19
         >>   38 POP_BLOCK

  5      >>   39 LOAD_FAST                1 (total)
              42 RETURN_VALUE

print fn_terse.func_name
dis.dis(fn_terse)

fn_terse
  8            0 LOAD_GLOBAL              0 (sum)
               3 LOAD_GLOBAL              1 (range)
               6 LOAD_FAST                0 (upper)
               9 CALL_FUNCTION            1
              12 CALL_FUNCTION            1
              15 RETURN_VALUE
