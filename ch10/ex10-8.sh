# 예제 10-8 클러스터에 새로운 컴퓨터가 들어와 있는지 테스트하기

$ ipython --profile=mycluster
Python 3.4.5 |Anaconda custom (x86_64)| (default, Jul  2 2016, 17:47:57)
Type "copyright", "credits" or "license" for more information.
...
In [1]: import ipyparallel as ipp

In [2]: ipp.Client()

In [3]: c.ids
Out[3]: [0, 1, 2, 3, 4]

In [4]: dview=c[:]

In [5]: with dview.sync_imports():
   ...:    import sys

In [6]: dview.apply_sync(lambda:sys.version)
Out[6]:
['3.4.5 |Anaconda custom (x86_64)| (default, Jul  2 2016, 17:47:57) \n[GCC 4.2.1
                                   Compatible Apple LLVM 4.2 (clang-425.0.28)]',
 '3.4.5 |Anaconda custom (x86_64)| (default, Jul  2 2016, 17:47:57) \n[GCC 4.2.1
                                   Compatible Apple LLVM 4.2 (clang-425.0.28)]',
 '3.4.5 |Anaconda custom (x86_64)| (default, Jul  2 2016, 17:47:57) \n[GCC 4.2.1
                                   Compatible Apple LLVM 4.2 (clang-425.0.28)]'
 '3.4.5 |Anaconda custom (x86_64)| (default, Jul  2 2016, 17:47:57) \n[GCC 4.2.1
                                   Compatible Apple LLVM 4.2 (clang-425.0.28)]']
