# 정체성 (Identity)
a = [1, 2, 3]
b = a
print(a is b)  # True, a와 b는 같은 리스트 객체를 참조

# 동질성 (Equality)
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True, a와 b는 내용이 동일

# 별명 (Aliasing)
a = [1, 2, 3]
b = a  # b는 a의 별명
b.append(4)
print(a)  # [1, 2, 3, 4], a도 변경됨