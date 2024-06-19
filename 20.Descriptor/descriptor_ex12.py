class LoggedAccess:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        value = instance.__dict__[self.name]
        print(f"Accessing {self.name}, value = {value}")
        return value

    def __set__(self, instance, value):
        print(f"Updating {self.name} to {value}")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print(f"Deleting {self.name}")
        del instance.__dict__[self.name]


class Person:
    age = LoggedAccess("age")

    def __init__(self, age):
        self.age = age


# 사용 예
p = Person(30)
print(p.age)  # 로그 출력 후 30 출력
p.age = 35  # 로그 출력
del p.age  # 로그 출력
'''
Updating age to 30
Accessing age, value = 30
30
Updating age to 35
Deleting age
'''