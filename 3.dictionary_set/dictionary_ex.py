person = {"name": "John", "age": 30}

print(person["name"])  # 출력: John
print(person["age"])   # 출력: 30

# 기본 구조
# {키: 값 for 아이템 in 시퀀스 if 조건}

# 기본 사용법
numbers = [1, 2, 3, 4]
squared_cubed = {x: x**3 for x in numbers}
print(squared_cubed)

# 조건을 포함한 사용법
even_square = {x**2: x for x in numbers if x % 2 == 0}
print(even_square)

# 기본 사용법
# value = dictionary.setdefault(key, default_value)

# 사람의 이름과 이메일이 저장된 딕셔너리
emails = {
    "John Doe": "johndoe@example.com",
    "Jane Smith": "janesmith@example.com"
}

# "Alice Johnson"의 이메일을 조회하되, 존재하지 않는다면 기본 이메일을 설정
email = emails.setdefault("Alice Johnson", "default@example.com")
print(email)  # 출력: default@example.com

# 이제 emails 딕셔너리를 확인하면 "Alice Johnson"이 추가된다.
print(emails)
# 출력: {'John Doe': 'johndoe@example.com', 'Jane Smith': 'janesmith@example.com', 'Alice Johnson': 'default@example.com'}