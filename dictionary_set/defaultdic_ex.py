from collections import defaultdict
# 리스트를 기본값으로 사용하는 defaultdict 생성
string_list_map = defaultdict(list)

# "fruits" 키에 리스트 값 추가
string_list_map['fruits'].append('apple')
string_list_map['fruits'].append('banana')

# "vegetables" 키가 없으므로 자동으로 빈 리스트가 생성되고, 그 뒤에 값이 추가됨
string_list_map['vegetables'].append('carrot')

print(string_list_map)  # 출력: defaultdict(<class 'list'>, {'fruits': ['apple', 'banana'], 'vegetables': ['carrot']})