# 예제 6-11 벡터 연산 기능을 제외한 numpy 2차원 확산 방점식의 성능

4 perf stat -e cycles,stalled-cycles-frontend,stalled-cycles-backend,instructions,\
     cache-references,cache-misses,branches,branch-misses,task-clock,faults,\
     minor-faults,cs,migrations -r 3 python diffusion_numpy.py

Performance counter stats for 'python diffusion_numpy.py' (3 runs):

   48,923,515,604 cycles                       #   3.413 GHz
   24,901,979,501 stalled-cycles-frontend      #   50.90% frontend cycles idle
    6,585,982,510 stalled-cycles-backend       #   13.46% backend  cycles idle
   53,208,756,117 instructions                 #   1.09  insns per cycles
                                               #   0.47  stalled cycles per insn
       83,436,665 cache-references             #   5.821 M/sec
        1,211,229 cache-misses                 #   1.452 % of all cache refs
    4,428,225,111 branches                     #   308.926 M/sec
        3,716,789 branch-misses                #   0.08% of all branches
     14334.219862 task-clock                   #   0.999 CPUs utilized
          751,185 page-faults                  #   0.052 M/sec
          751,185 minor-faults                 #   0.052 M/sec
               24 context-switches             #   0.002 K/sec
                5 CPU-migrations               #   0.000 K/sec

     14.345794896 seconds time elapsed
