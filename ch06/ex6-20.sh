# 예제 6-20 numpy의 제자리 연산, 사용자 정의 laplacian 함수, numexpr을 사용했을 때의 성능 측정 결과

$ perf <emphasis role="strong">stat -e cycles,stalled-cycles-frontend,stalled-cycles-backend,instructions,\
     cache-references,cache-misses,branches,branch-misses,task-clock,faults,\
     minor-faults,cs,migrations -r 3 python diffusion_numpy_memory2_numexpr.py

Performance counter stats for 'python diffusion_numpy_memory2_numexpr.py' (3 runs):

    5,940,414,581 cycles                       #   1.447 GHz
    3,706,635,857 stalled-cycles-frontend      #   62.40% frontend cycles idle
    2,321,606,960 stalled-cycles-backend       #   36.08% backend  cycles idle
    6,909,546,082 instructions                 #   1.16  insns per cycles
                                               #   0.54  stalled cycles per insn
      261,136,786 cache-references             #   63.628 M/sec
       11,623,783 cache-misses                 #   4.451 % of all cache refs
      627,319,686 branches                     #   152.851 M/sec
        8,443,876 branch-misses                #   1.35% of all branches
      4104.127508 task-clock                   #   1.364 CPUs utilized
            9,786 page-faults                  #   0.002 M/sec
            9,786 minor-faults                 #   0.002 M/sec
            8,701 context-switches             #   0.002 K/sec
               60 CPU-migrations               #   0.015 K/sec

      3.009811418 seconds time elapsed
