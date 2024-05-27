from typing import Protocol


class Serializable(Protocol):
    def serialize(self) -> str:
        ...


class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age


def user_serialize(self) -> str:
    return f"User(username={self.username}, age={self.age})"


User.serialize = user_serialize

# 이제 User 클래스는 Serializable 프로토콜을 따른다
user = User("Alice", 30)
print(user.serialize())  # 출력: User(username=Alice, age=30)
