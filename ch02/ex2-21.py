# 예제 2-21 단위 테스트를 위해 네임스페이스에 no-op @profiler 데코레이터 추가하기(line_profiler)

# line_profiler용
if '__builtin__' not in dir() or not hasattr(__builtin__, 'profile'):
    def profile(func):
        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        return inner
