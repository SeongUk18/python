class JSONObject:
    def __init__(self, data):
        for key, value in data.items():
            if isinstance(value, dict):
                value = JSONObject(value)  # 중첩된 dict를 JSONObject로 변환
            setattr(self, key, value)

    def __repr__(self):
        return f"JSONObject({self.__dict__})"


# JSON 데이터 예제
json_data = {
    "name": "Alice",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Wonderland"
    },
    "hobbies": ["reading", "chess"]
}

# JSON 데이터를 JSONObject로 변환
json_obj = JSONObject(json_data)

# 동적 속성을 이용한 데이터 접근
print(json_obj.name)  # 출력: Alice
print(json_obj.age)   # 출력: 30
print(json_obj.address.street)  # 출력: 123 Main St
print(json_obj.hobbies)  # 출력: ['reading', 'chess']
