# ==
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True, 내용이 동일하기 때문

x = 10
y = 10.0
print(x == y)  # True, 값이 같기 때문 (정수 10과 부동소수점 10.0)

# is
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)  # True, b는 a와 동일한 객체
print(a is c)  # False, c는 a와 같은 값을 가지지만, 다른 객체