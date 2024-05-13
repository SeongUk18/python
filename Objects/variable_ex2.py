# 정체성 (Identity)
a = 42
print(id(a))  # 예: 2874709077584

# 자료형 (Type)
a = 42
print(type(a))  # <class 'int'>

# 값 (Value)
a = 42   # a는 정수 42를 값으로 가짐
b = "hello"  # b는 문자열 "hello"를 값으로 가짐

# 정체성 비교: is 연산자
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)  # True, a와 b는 동일한 객체
print(a is c)  # False, a와 c는 내용은 같지만 다른 객체