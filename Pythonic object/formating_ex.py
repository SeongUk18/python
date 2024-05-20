# %
name = "Alice"
age = 30
print("Name: %s, Age: %d" % (name, age)) # Name: Alice, Age: 30

# str.format()
name = "Alice"
age = 30
print("Name {}, Age: {}".format(name, age)) # Name: Alice, Age: 30
print("Name {0}, Age: {1}".format(name, age)) # Name: Alice, Age: 30
print("Name {name}, Age: {age}".format(name=name, age=age)) # Name: Alice, Age: 30

# f-strings
name = "Alice"
age = 30
print(f"Name: {name}, Age: {age}") # Name: Alice, Age: 30

# 숫자 포멧팅
value = 1234.5678
print(f"Value: {value:.2f}") # Value: 1234.57
print(f"Value: {value:,.2f}") # Value: 1,234.57

# 정렬
name = "Alice"
print(f"Name: {name:<10}") # Name: Alice
print(f"Name: {name:>10}") # Name:      Alice
print(f"Name: {name:^10}") # Name:   Alice

# 채우기
name = "Alice"
print(f"Name: {name:_<10}") # Name: Alice_____
