# 예제 6-8 메모리 할당을 줄인 2차원 확산 파이썬 방정식 코드의 성능 측정 결과

$ perf stat -e cycles,stalled-cycles-frontend,stalled-cycles-backend,instructions,\
     cache-references,cache-misses,branches,branch-misses,task-clock,faults,\
     minor-faults,cs,migrations -r 3 python diffusion_python_memory.py

Performance counter stats for 'python diffusion_python_memory.py' (3 runs):

  329,155,359,015 cycles                       #   3.477 GHz
   76,800,457,550 stalled-cycles-frontend      #   23.33% frontend cycles idle
   46,556,100,820 stalled-cycles-backend       #   14.14% backend  cycles idle
  598,135,111,009 instructions                 #   1.82  insns per cycle
                                               #   0.13  stalled cycles per insn
       35,497,196 cache-references             #   0.375 M/sec
       10,716,972 cache-misses                 #   30.191 % of all cache refs
  133,881,241,254 branches                     #   1414.067 M/sec
    2,891,093,384 branch-misses                #   2.16% of all branches
     94678.127621 task-clock                   #   0.999 CPUs utilized
            5,439 page-faults                  #   0.057 K/sec
            5,439 minor-faults                 #   0.057 K/sec
              125 context-switches             #   0.001 K/sec
                6 CPU-migrations               #   0.000 K/sec

     94.749389121 seconds time elapsed
