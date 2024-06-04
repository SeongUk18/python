def generator1():
    yield from range(5)
    yield from "abc"


# Usage
for value in generator1():
    print(value)

'''
0
1
2
3
4
a
b
c
'''