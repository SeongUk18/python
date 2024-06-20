class Descriptor:
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        print(f"Getting {self.name}")
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print(f"Setting {self.name} to {value}")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print(f"Deleting {self.name}")
        del instance.__dict__[self.name]


class ValidatedDescriptor(Descriptor):
    def __init__(self, name=None, validator=None):
        self.validator = validator
        super().__init__(name)

    def __set__(self, instance, value):
        if self.validator and not self.validator(value):
            raise ValueError(f"Invalid value for {self.name}: {value}")
        super().__set__(instance, value)


def positive_validator(value):
    return value > 0


def add_validated_descriptor(cls):
    for key, value in cls.__dict__.items():
        if isinstance(value, ValidatedDescriptor):
            value.name = key
    return cls


@add_validated_descriptor
class MyValidatedClass:
    positive_attr = ValidatedDescriptor(validator=positive_validator)


# 인스턴스 생성
validated_instance = MyValidatedClass()

# 유효한 값 설정
validated_instance.positive_attr = 10  # 출력: Setting positive_attr to 10

# 유효하지 않은 값 설정
try:
    validated_instance.positive_attr = -5  # ValueError 발생
except ValueError as e:
    print(e)  # 출력: Invalid value for positive_attr: -5
