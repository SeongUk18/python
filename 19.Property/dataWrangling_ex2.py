class DataObject:
    def __init__(self, name, value):
        self.name = name
        self.value = value


data = DataObject("sample", 10)
setattr(data, 'new_attr', 20)
print(data.new_attr)  # 출력: 20

value = getattr(data, 'new_attr')
print(value)  # 출력: 20
