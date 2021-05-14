# 예제 6-15 numpy와 제자리 연산을 활용한 경우의 성능 측정 결과

$ perf stat -e cycles,stalled-cycles-frontend,stalled-cycles-backend,instructions,\
     cache-references,cache-misses,branches,branch-misses,task-clock,faults,\
     minor-faults,cs,migrations -r 3 python diffusion_numpy_memory.py

Performance counter stats for 'python diffusion_numpy_memory.py' (3 runs):

    7,864,072,570 cycles                       #   3.330 GHz
    3,055,151,931 stalled-cycles-frontend      #   38.85% frontend cycles idle
    1,368,235,506 stalled-cycles-backend       #   17.40% backend  cycles idle
   13,257,488,848 instructions                 #   1.69  insns per cycles
                                               #   0.23  stalled cycles per insn
      239,195,407 cache-references             #   101.291 M/sec
        2,886,525 cache-misses                 #   1.207 % of all cache refs
    3,166,506,861 branches                     #   1340.903 M/sec
        3,204,960 branch-misses                #   0.10% of all branches
      2361.473922 task-clock                   #   0.999 CPUs utilized
            6,527 page-faults                  #   0.093 M/sec
            6,527 minor-faults                 #   0.003 M/sec
                6 context-switches             #   0.003 K/sec
                2 CPU-migrations               #   0.001 K/sec

      2.363727876 seconds time elapsed
