from typing import Protocol


class Serializable(Protocol):
    def serialize(self) -> str:
        ...


class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age

    def serialize(self) -> str:
        return f"User(username={self.username}, age={self.age})"


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def serialize(self) -> str:
        return f"Product(name={self.name}, price={self.price})"


def save_to_file(obj: Serializable) -> None:
    serialized_data = obj.serialize()
    print(f"Saving data: {serialized_data}")


user = User("Alice", 30)
product = Product("Laptop", 1500.0)

save_to_file(user)     # 출력: Saving data: User(username=Alice, age=30)
save_to_file(product)  # 출력: Saving data: Product(name=Laptop, price=1500.0)
