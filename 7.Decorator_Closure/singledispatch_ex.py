from functools import singledispatch

@singledispatch
def say(data):
    print(f"data: {data}")

@say.register(int)
def _(data):
    print(f"int: {data}")

@say.register(list)
def _(data):
    print(f"list: {data}")

say("Hello")  # data: Hello
say(123)      # int: 123
say([1, 2, 3])  # list: [1, 2, 3]