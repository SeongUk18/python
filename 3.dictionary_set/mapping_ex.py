from collections import OrderedDict, defaultdict, ChainMap, Counter
from types import MappingProxyType

# OrderedDict 예시
ordered = OrderedDict([('a', 1), ('b', 2)])
ordered.move_to_end('a')  # 키 'a'를 마지막으로 이동
print(ordered)

# defaultdict 예시
default = defaultdict(int)
default['a'] += 1
print(default)

# ChainMap 예시
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
chain = ChainMap(dict1, dict2)
print(chain['b'])  # 출력: 2 (첫 번째 매핑에서 'b'의 값)

# Counter 예시
counter = Counter('banana')
print(counter)  # 출력: Counter({'a': 3, 'b': 1, 'n': 2})

# MappingProxyType 예시
original = {'a': 1}
proxy = MappingProxyType(original)
print(proxy['a'])  # 출력: 1
# proxy['a'] = 2  # TypeError: 'mappingproxy' object does not support item assignment