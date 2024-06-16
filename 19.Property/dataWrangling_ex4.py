import pandas as pd


class DataFrameRow:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


df = pd.DataFrame({
    'name': ['Alice', 'Bob'],
    'age': [30, 25]
})

objects = [DataFrameRow(**row) for index, row in df.iterrows()]

for obj in objects:
    print(obj.name, obj.age)
# 출력:
# Alice 30
# Bob 25
