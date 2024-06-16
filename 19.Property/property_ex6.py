class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15°C is not possible")
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9 / 5) + 32


# 예제 사용
temp = Temperature(25)
print(temp.celsius)      # 25
print(temp.fahrenheit)   # 77.0

temp.celsius = 30
print(temp.celsius)      # 30
print(temp.fahrenheit)   # 86.0

try:
    temp.celsius = -300
except ValueError as e:
    print(e)  # Temperature below -273.15°C is not possible
    