def property_factory(private_name, validation_func=None):
    def getter(self):
        return getattr(self, private_name)

    def setter(self, value):
        if validation_func:
            if not validation_func(value):
                raise ValueError(f"Invalid value for {private_name}")
        setattr(self, private_name, value)

    return property(getter, setter)


class Product:
    def __init__(self, name, price, discount):
        self._name = name
        self._price = price
        self._discount = discount

    # 이름 프로퍼티 정의
    name = property_factory('_name')

    # 가격 프로퍼티 정의 (음수가 아닌지 검증)
    price = property_factory('_price', lambda v: v >= 0)

    # 할인율 프로퍼티 정의 (0과 1 사이의 값인지 검증)
    discount = property_factory('_discount', lambda v: 0 <= v <= 1)


# 예제 사용
product = Product("Laptop", 1000, 0.1)

print(product.name)     # Laptop
print(product.price)    # 1000
print(product.discount) # 0.1

product.price = 1200    # 정상 작동
print(product.price)    # 1200

try:
    product.price = -200  # 예외 발생
except ValueError as e:
    print(e)  # Price must be non-negative

try:
    product.discount = 1.5  # 예외 발생
except ValueError as e:
    print(e)  # Discount must be between 0 and 1
    