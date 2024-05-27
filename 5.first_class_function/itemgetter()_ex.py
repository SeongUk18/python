# 리스트에서 아이템 가져오기
from operator import itemgetter

data = [5, 1, 2, 9, 8]
get_third_item = itemgetter(2)
print(get_third_item(data))  # 출력: 2

# 딕셔너리에서 여러 키의 값 가져오기
record = {'name': 'John', 'age': 45, 'job': 'Engineer'}
get_name_and_job = itemgetter('name', 'job')
print(get_name_and_job(record))  # 출력: ('John', 'Engineer')

# 고급 사용법: 여러 인덱스 접근
# itemgetter()에 여러 인덱스를 넘겨주면, 해당 인덱스들의 아이템을 튜플 형태로 반환함.
data = [5, 1, 2, 9, 8]
get_multiple_items = itemgetter(0, 3, 4)
print(get_multiple_items(data))  # 출력: (5, 9, 8)

# 객체 리스트를 특정 속성으로 정렬하기
records = [
    {'name': 'John', 'score': 90},
    {'name': 'Jane', 'score': 88},
    {'name': 'Dave', 'score': 92}
]

# 점수(score)를 기준으로 정렬
sorted_records = sorted(records, key=itemgetter('score'))
print(sorted_records)  # 점수가 낮은 순으로 정렬된 리스트 출력