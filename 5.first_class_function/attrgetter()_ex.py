# 객체의 속성 가져오기
from operator import attrgetter

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("John", 30)
get_name = attrgetter('name')
print(get_name(person))  # 출력: John

# 고급 사용법: 여러 속성 접근
person = Person("Alice", 25)
get_name_and_age = attrgetter('name', 'age')
print(get_name_and_age(person))  # 출력: ('Alice', 25)

# 객체 리스트를 특정 속성으로 정렬하기
people = [
    Person("John", 30),
    Person("Jane", 25),
    Person("Dave", 35)
]

# 나이(age)를 기준으로 정렬
sorted_people = sorted(people, key=attrgetter('age'))
print([(p.name, p.age) for p in sorted_people])  # 나이가 낮은 순으로 출력

# 중첩 속성 접근
# attrgetter()는 또한 중첩된 속성에 접근할 수 있는 기능을 제공한다. 예를 들어, attrgetter('a.b.c')는 obj.a.b.c와 동일하게 작동한다.
class Department:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

dept = Department("Finance")
emp = Employee("John", dept)
get_dept_name = attrgetter('department.name')
print(get_dept_name(emp))  # 출력: Finance