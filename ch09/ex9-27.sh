# 예제 9-27 pmap과 ps를 사용해 운영 체제가 프로세스를 어떻게 보는지 조사하기

$ ps -A -o pid,size,vsize,cmd | grep np_shared
11268 232464 6564988 python np_shared.py
11288 11232 6343756 python np_shared.py
11278 11228 6343752 python np_shared.py
11290 11228 6343752 python np_shared.py
11291 11228 6343752 python np_shared.py

$ pmap -x 11268 | grep s-
Address           Kbytes     RSS   Dirty Mode   Mapping
00007f1953663000 6250000 6250000 6250000 rw-s- zero (deleted)
...

$ pmap -x 11288 | grep s-
Address           Kbytes     RSS   Dirty Mode   Mapping
00007f1953663000 6250000 1562512 1562512 rw-s- zero (deleted)
...
