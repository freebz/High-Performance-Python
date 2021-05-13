# 예제 5-1 파이썬 for 루프 재구성하기

# 다음 파이썬 루프는
for i in object:
    do_work(i)

# 아래 코드와 동일하다.
object_iterator = iter(object)
while True:
    try:
        i = object_iterator.next()
        do_work(i)
    except StopIteration:
        break
