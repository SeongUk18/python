# [:]을 이용한 복사
original = [1, 2, [3, 4]]
copied = original[:]

print(original == copied)  # True, 내용이 같음
print(original is copied)  # False, 다른 객체임

# 내부 리스트 변경
original[2].append(5)
print(copied)  # [1, 2, [3, 4, 5]], 내부 리스트 변경이 복사본에도 반영됨

# 얕은 복사
import copy

original = [1, 2, [3, 4]]
shallow = copy.copy(original)
shallow[2].append(5)

print(original)  # [1, 2, [3, 4, 5]]
print(shallow)   # [1, 2, [3, 4, 5]]

# 깊은 복사 (Deep Copy)
import copy

original = [1, 2, [3, 4]]
deep = copy.deepcopy(original)
deep[2].append(5)

print(original)  # [1, 2, [3, 4]]
print(deep)       # [1, 2, [3, 4, 5]]