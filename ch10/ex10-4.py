# 예제 10-4 원격 엔진에 모듈 임포트하기

in [5]: dview = c[:] # 직접 뷰다(즉, 부하 분산 뷰가 아니다).

in [6]: with dview.sync_imports():
    ....: import os
    ....:
importing os on engine(s)

In [7]: dview.apply_sync(lambda:os.getpid())
Out[7]: [15079, 15080, 15081, 15089]

In [8]: dview.execute("import sys") # 명령을 원격 실행하는 또 다른 방법
