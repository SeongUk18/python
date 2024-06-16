class DataCleaner:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def clean(self):
        for attr in list(self.__dict__.keys()):
            if getattr(self, attr) is None:
                delattr(self, attr)


raw_data = {
    'name': 'Charlie',
    'age': None,
    'email': 'charlie@example.com'
}

cleaner = DataCleaner(**raw_data)
cleaner.clean()
print(cleaner.__dict__)  # 출력: {'name': 'Charlie', 'email': 'charlie@example.com'}
