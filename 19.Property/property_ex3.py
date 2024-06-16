class MyClass:
    def __init__(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def set_value(self, value):
        if value < 0:
            raise ValueError("Value must be non-negative")
        self._value = value

    def del_value(self):
        del self._value

    value = property(get_value, set_value, del_value, "I'm the 'value' property.")