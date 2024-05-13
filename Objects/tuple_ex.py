# 튜플의 불변성
t = (1, 2, 3)
# t[0] = 10  # 이 코드는 TypeError를 발생시킨다.

# 상대적 불변성
t = ([1, 2, 3], 'a', 'b')
t[0].append(4)  # 튜플 내부의 리스트는 가변 객체이므로 변경할 수 있다.
print(t)  # ([1, 2, 3, 4], 'a', 'b')
# t[1] = 'new'  # 이 코드는 여전히 TypeError를 발생시킨다.

# 상대적 불변성 2
# 두 튜플 생성
t1 = ([1, 2, 3], 'a', 'b')
t2 = ([1, 2, 3], 'a', 'b')

# 튜플 t1과 t2의 전체 비교
print(t1 == t2)  # True, 튜플 내용이 동일하기 때문

# 튜플 내 리스트의 id 비교
print(id(t1[0]), id(t2[0]))  # 두 리스트의 메모리 주소가 다름을 확인 # 2053409528384 2053409420416

# 튜플 내 리스트의 내용 변경
t1[0].append(4)
print(t1)  # ([1, 2, 3, 4], 'a', 'b')
print(t2)  # ([1, 2, 3], 'a', 'b')

# 변경 후 튜플 t1과 t2의 전체 비교
print(t1 == t2)  # False, 리스트 내용이 변경되었기 때문