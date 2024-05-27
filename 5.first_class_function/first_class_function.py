# 함수를 변수에 할당
def greet(name):
    return f"Hello, {name}!"

greet_someone = greet  # 함수를 다른 변수에 할당
print(greet_someone("Alice"))  # 'Hello, Alice!'

# 함수를 인수로 전달ㅁ
def greet(name):
    return f"Hello, {name}!"

def loud_greeting(func, name):
    return func(name).upper()

print(loud_greeting(greet, "Bob"))  # 'HELLO, BOB!'

# 함수에서 함수 반환
def make_greeter(greeting):
    def greeter(name):
        return f"{greeting}, {name}!"
    return greeter

hello_greeter = make_greeter("Hello")
print(hello_greeter("Charlie"))  # 'Hello, Charlie!'