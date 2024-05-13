# __copy__() 메소드
import copy

class MyClass:
    def __init__(self, value):
        self.value = value

    def __copy__(self):
        # 새로운 객체를 생성하고 초기화
        cls = self.__class__
        result = cls.__new__(cls)
        result.value = self.value
        return result

obj = MyClass(10)
copied_obj = copy.copy(obj)

print(copied_obj.value)  # 10

# __deepcopy__() 메소드
import copy

class MyClass:
    def __init__(self, value):
        self.value = value

    def __deepcopy__(self, memo):
        print("deepcopy 호출됨")
        # 새로운 객체를 생성하고 초기화
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        result.value = copy.deepcopy(self.value, memo)
        return result

obj = MyClass([1, 2, 3])
deep_copied_obj = copy.deepcopy(obj)
# deepcopy 호출됨
print(deep_copied_obj.value)  # [1, 2, 3]