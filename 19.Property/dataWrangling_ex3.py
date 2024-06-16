class FlexibleData:
    def __init__(self, data):
        for key, value in data.items():
            setattr(self, key, value)


data = {
    'name': 'Alice',
    'age': 30,
    'country': 'Wonderland'
}

flexible_data = FlexibleData(data)
print(flexible_data.name)  # 출력: Alice
print(flexible_data.age)   # 출력: 30
print(flexible_data.country)  # 출력: Wonderland
