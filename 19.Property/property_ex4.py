class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        """I'm the 'value' property."""
        return self._value

    @value.setter
    def value(self, value):
        if value < 0:
            raise ValueError("Value must be non-negative")
        self._value = value

    @value.deleter
    def value(self):
        del self._value
