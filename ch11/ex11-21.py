# 예제 11-21 모리스 카운터 라이브러리 예제

In [2]: mc = MorrisCounter()
In [3]: print(len(mc))
1.0
In [4]: mc.add() # P(1)의 덧셈
In [5]: print(len(mc))
2.0
In [6]: mc.add() # P(0.5)의 덧셈
In [7]: print(len(mc)) # 이번에는 덧셈이 발생하지 않았다.
2.0
