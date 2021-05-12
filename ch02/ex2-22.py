# 예제 2-22 단위 테스트를 위해 네임스페이스에 no-op @profiler 데코레이터 추가하기(memory_profiler)

# memory_profiler용
if 'profile' not in dir():
    def profile(func):
        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        return inner
