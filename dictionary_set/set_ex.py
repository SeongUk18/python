a = {1, 2, 3}
b = {3, 4, 5}

# 합집합
print(a | b)  # {1, 2, 3, 4, 5}

# 교집합
print(a & b)  # {3}

# 차집합
print(a - b)  # {1, 2}

# 대칭 차집합
print(a ^ b)  # {1, 2, 4, 5}

fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])

# 합집합
print(fs1 | fs2)  # frozenset({1, 2, 3, 4, 5})

# 교집합
print(fs1 & fs2)  # frozenset({3})

# 차집합
print(fs1 - fs2)  # frozenset({1, 2})

# 대칭 차집합
print(fs1 ^ fs2)  # frozenset({1, 2, 4, 5})


# 합집함
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # {1, 2, 3, 4, 5}
print(a.union(b))  # {1, 2, 3, 4, 5}

# 교집합
print(a & b)  # {3}
print(a.intersection(b))  # {3}

# 차집합
print(a - b)  # {1, 2}
print(a.difference(b))  # {1, 2}

# 대칭 차집합
print(a ^ b)  # {1, 2, 4, 5}
print(a.symmetric_difference(b))  # {1, 2, 4, 5}

# 부분 집합, 상위 집합 확인
c = {1, 2}
print(c <= a)  # True
print(c.issubset(a))  # True
print(a >= c)  # True
print(a.issuperset(c))  # True

# 요소 추가 및 제거
a.add(6)
print(a)  # {1, 2, 3, 6}
a.discard(6)
print(a)  # {1, 2, 3}
a.pop()
print(a)  # {2, 3}