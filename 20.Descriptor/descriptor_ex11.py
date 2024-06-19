class Positive:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.name] = value
        else:
            raise ValueError(f"{self.name} must be > 0")

    def __delete__(self, instance):
        raise AttributeError("Cannot delete attribute")


class Product:
    price = Positive("price")

    def __init__(self, price):
        self.price = price


# 사용 예
item = Product(10)
print(item.price)  # 10 출력
try:
    item.price = -5  # ValueError 발생
except ValueError as e:
    print(e)  # "price must be > 0" 출력
