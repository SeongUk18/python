class Example:
    def __init__(self):
        self.__private_var = "I am private"
        self._protected_var = "I am protected"
        self.public_var = "I am public"

    def __private_method(self):
        return "This is a private method"

    def _protected_method(self):
        return "This is a protected method"

    def public_method(self):
        return "This is a public method"

    def access_methods(self):
        return self.__private_method(), self._protected_method(), self.public_method()


e = Example()

# 직접 접근
# print(e.__private_var)  # AttributeError: 'Example' object has no attribute '__private_var'
print(e._protected_var)  # I am protected
print(e.public_var)  # I am public

# 이름 장식을 통해 접근 (권장되지 않음)
print(e._Example__private_var)  # I am private

# 메서드 접근
# print(e.__private_method())  # AttributeError: 'Example' object has no attribute '__private_method'
print(e._protected_method())  # This is a protected method
print(e.public_method())  # This is a public method

# 이름 장식을 통해 접근 (권장되지 않음)
print(e._Example__private_method())  # This is a private method

# 내부 메서드 접근
print(e.access_methods())  # ('This is a private method', 'This is a protected method', 'This is a public method')
