# 예제 6-10 numpy를 사용한 2차원 확산 방점식의 성능 측정

$ perf stat -e cycles,stalled-cycles-frontend,stalled-cycles-backend,instructions,\
     cache-references,cache-misses,branches,branch-misses,task-clock,faults,\
     minor-faults,cs,migrations -r 3 python diffusion_numpy.py

Performance counter stats for 'python diffusion_numpy.py' (3 runs):

   10,194,811,718 cycles                       #   3.332 GHz
    4,435,850,419 stalled-cycles-frontend      #   43.51% frontend cycles idle
    2,055,861,567 stalled-cycles-backend       #   20.17% backend  cycles idle
   15,165,151,844 instructions                 #   1.49  insns per cycles
                                               #   0.29  stalled cycles per insn
      346,798,311 cache-references             #   113.362 M/sec
          519,793 cache-misses                 #   0.150 % of all cache refs
    3,506,887,927 branches                     #   1146.334 M/sec
        3,681,441 branch-misses                #   0.10% of all branches
      3059.219862 task-clock                   #   0.999 CPUs utilized
          751,707 page-faults                  #   0.246 M/sec
          751,707 minor-faults                 #   0.246 M/sec
                8 context-switches             #   0.003 K/sec
                1 CPU-migrations               #   0.000 K/sec

      3.061883218 seconds time elapsed
