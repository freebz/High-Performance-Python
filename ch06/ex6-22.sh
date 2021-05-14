# 예제 6-22 scipy의 laplace 함수를 사용한 확산 방점식의 성능 측정 결과

$ perf stat -e cycles,stalled-cycles-frontend,stalled-cycles-backend,instructions,\
     cache-references,cache-misses,branches,branch-misses,task-clock,faults,\
     minor-faults,cs,migrations -r 3 python diffusion_scipy.py

Performance counter stats for 'python diffusion_scipy.py' (3 runs):

    6,573,168,470 cycles                       #   2.929 GHz
    3,574,258,872 stalled-cycles-frontend      #   54.38% frontend cycles idle
    2,357,614,687 stalled-cycles-backend       #   35.87% backend  cycles idle
    9,850,025,585 instructions                 #   1.50  insns per cycles
                                               #   0.36  stalled cycles per insn
      415,930,123 cache-references             #   185.361 M/sec
        3,188,390 cache-misses                 #   0.767 % of all cache refs
    1,608,887,891 branches                     #   717.006 M/sec
        4,017,205 branch-misses                #   0.25% of all branches
      2243.897843 task-clock                   #   0.994 CPUs utilized
            7,319 page-faults                  #   0.003 M/sec
            7,319 minor-faults                 #   0.003 M/sec
               12 context-switches             #   0.005 K/sec
                1 CPU-migrations               #   0.000 K/sec

      2.258396667 seconds time elapsed
