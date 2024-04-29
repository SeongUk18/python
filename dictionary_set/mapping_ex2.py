from types import MappingProxyType

writable = {'one': 1, 'two': 2}
read_only = MappingProxyType(writable)

# 값을 읽는 것은 가능
print(read_only['one'])  # 출력: 1

# 값을 변경하려고 시도하면 오류 발생
# read_only['one'] = 11  # TypeError: 'mappingproxy' object does not support item assignment

# 새 키를 추가하려고 시도하면 오류 발생
# read_only['three'] = 3  # TypeError: 'mappingproxy' object does not support item assignment