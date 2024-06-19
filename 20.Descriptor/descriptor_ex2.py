class Quantity:
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


class LineItem:
    quantity = Quantity("quantity")
    price = Quantity("price")

    def __init__(self, description, quantity, price):
        self.description = description
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.quantity * self.price


# 사용 예
item = LineItem("Apple", 10, 1.5)
print(item.total())  # 15.0 출력

# 유효성 검사
try:
    item.quantity = -1  # ValueError 발생
except ValueError as e:
    print(e)  # "quantity must be > 0" 출력
