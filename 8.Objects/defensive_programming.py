# 데이터 복사
import copy

def process_data(data):
    # 데이터의 깊은 복사본을 만들어 작업 수행
    data_copy = copy.deepcopy(data)
    # 데이터 처리 로직
    data_copy.append("new data")
    return data_copy

original_data = [1, 2, 3]
new_data = process_data(original_data)
print(original_data)  # [1, 2, 3] - 원본 데이터 유지
print(new_data)       # [1, 2, 3, "new data"] - 변경된 데이터

# 매개변수 유효성 검사
def add_item(items, item):
    if not isinstance(items, list):
        raise ValueError("items must be a list.")
    if item in items:
        raise ValueError("item already exists.")
    items.append(item)

try:
    current_items = [1, 2, 3]
    add_item(current_items, 2)
except ValueError as e:
    print(e)  # item already exists.