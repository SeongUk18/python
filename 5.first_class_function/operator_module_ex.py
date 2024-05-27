import operator

result_add = operator.add(10, 5)  # 15
result_mul = operator.mul(10, 5)  # 50

result_lt = operator.lt(10, 20)  # True
result_eq = operator.eq(10, 10)  # True

result_and = operator.and_(True, False)  # False

lst = [1, 2, 3, 4]
result_item = operator.getitem(lst, 2)  # 3

class Person:
    def __init__(self, name):
        self.name = name

person = Person("John")
name = operator.attrgetter('name')(person)  # 'John'
