# wrong ex
def append_to(element, to=[]):
    to.append(element)
    return to

print(append_to(12))  # [12]
print(append_to(34))  # [12, 34]

# right ex
def append_to(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to

print(append_to(12))  # [12]
print(append_to(34))  # [34]

# class ver: wrong ex
class DataCollector:
    def __init__(self, data=[]):
        self.data = data

    def add_data(self, value):
        self.data.append(value)

# 객체 생성
collector1 = DataCollector()
collector1.add_data(1)
collector1.add_data(2)

# 또 다른 객체 생성
collector2 = DataCollector()
collector2.add_data(3)

# 각 객체의 데이터 출력
print("Collector 1 data:", collector1.data)  # [1, 2, 3] - 의도치 않은 결과!
print("Collector 2 data:", collector2.data)  # [1, 2, 3] - 의도치 않은 결과!

# class ver: right ex
class DataCollector:
    def __init__(self, data=None):
        if data is None:
            data = []
        self.data = data

    def add_data(self, value):
        self.data.append(value)

# 객체 생성
collector1 = DataCollector()
collector1.add_data(1)
collector1.add_data(2)

# 또 다른 객체 생성
collector2 = DataCollector()
collector2.add_data(3)

# 각 객체의 데이터 출력
print("Collector 1 data:", collector1.data)  # [1, 2] - 올바른 결과!
print("Collector 2 data:", collector2.data)  # [3] - 올바른 결과!