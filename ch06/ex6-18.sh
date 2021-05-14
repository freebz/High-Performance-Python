# 예제 6-18 numpy를 이용한 제자리 연산과 커스텀 라플라시안(laplacian) 함수를 사용했을 때의 성능 측정 결과

$ perf stat -e cycles,stalled-cycles-frontend,stalled-cycles-backend,instructions,\
     cache-references,cache-misses,branches,branch-misses,task-clock,faults,\
     minor-faults,cs,migrations -r 3 python diffusion_numpy_memory2.py

Performance counter stats for 'python diffusion_numpy_memory2.py' (3 runs):

    4,303,799,244 cycles                       #   3.108 GHz
    2,814,678,053 stalled-cycles-frontend      #   65.40% frontend cycles idle
    1,635,172,736 stalled-cycles-backend       #   37.99% backend  cycles idle
    4,631,882,411 instructions                 #   1.88  insns per cycles
                                               #   0.61  stalled cycles per insn
      272,151,957 cache-references             #   196.563 M/sec
        2,835,948 cache-misses                 #   1.042 % of all cache refs
      621,565,054 branches                     #   448.928 M/sec
        2,905,879 branch-misses                #   0.47% of all branches
      1384.555494 task-clock                   #   0.999 CPUs utilized
            5,559 page-faults                  #   0.004 M/sec
            5,559 minor-faults                 #   0.004 M/sec
                6 context-switches             #   0.004 K/sec
                3 CPU-migrations               #   0.002 K/sec

      1.386148918 seconds time elapsed
