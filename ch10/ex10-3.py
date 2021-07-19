# 예제 10-3 IPython에서 로컬 엔진을 사용할 수 있는지 검사하기

In [1]: import ipyparallel as ipp

In [2]: c = ipp.Client()

In [3]: print(c.ids)
[0, 1, 2, 3]

In [4]: c[:].apply_sync(lambda:"Hello High Performance Pythonistas!")
Out[4]:
['Hello High Performance Pythonistas!',
 'Hello High Performance Pythonistas!',
 'Hello High Performance Pythonistas!',
 'Hello High Performance Pythonistas!']
