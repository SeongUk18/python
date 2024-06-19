class CachedProperty:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.name not in instance.__dict__:
            instance.__dict__[self.name] = self.func(instance)
        return instance.__dict__[self.name]


class MyClass:
    @CachedProperty
    def expensive_computation(self):
        print("Computing value...")
        return 42


# 사용 예
obj = MyClass()
print(obj.expensive_computation)  # "Computing value..." 출력 후 42 출력
print(obj.expensive_computation)  # 42 출력 (캐시된 값 사용)
