# 예제 7-5 setup.py를 실행해서 컴파일된 모듈을 새로 빌드하기

python setup.py build_ext --inplace
# running build_ext
# skipping 'cythonfn.c' Cython extension (up-to-date)
# building 'calculate' extension
# creating build
# creating build/temp.linux-x86_64-3.8
# x86_64-linux-gnu-gcc -pthread -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -g -fwrapv -O2 -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -I/usr/include/python3.8 -c cythonfn.c -o build/temp.linux-x86_64-3.8/cythonfn.o
# x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fwrapv -O2 -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fwrapv -O2 -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.8/cythonfn.o -o /home/fx/work/High Performance Python/ch07/calculate.cpython-38-x86_64-linux-gnu.so
