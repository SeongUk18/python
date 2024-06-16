# 예제 데이터
users_data = [
    {'user_id': 1, 'name': 'Alice'},
    {'user_id': 2, 'name': 'Bob'}
]

orders_data = [
    {'order_id': 1, 'user_id': 1, 'product': 'Laptop'},
    {'order_id': 2, 'user_id': 1, 'product': 'Mouse'},
    {'order_id': 3, 'user_id': 2, 'product': 'Keyboard'}
]


class Order:
    def __init__(self, order_id, user_id, product):
        self.id = order_id
        self.user_id = user_id
        self.product = product

    def __repr__(self):
        return f"Order(id={self.id}, user_id={self.user_id}, product='{self.product}')"


class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name

    @property
    def orders(self):
        # 'self.id'를 사용하여 관련된 주문을 필터링
        return [order for order in orders if order.user_id == self.id]

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}')"


# Order 객체 생성
orders = [Order(**order) for order in orders_data]

# User 객체 생성
users = [User(**user) for user in users_data]

# 각 사용자의 주문 출력
for user in users:
    print(f"User: {user.name}")
    print("Orders:")
    for order in user.orders:
        print(f"  - {order}")

'''
User: Alice
Orders:
  - Order(id=1, user_id=1, product='Laptop')
  - Order(id=2, user_id=1, product='Mouse')
User: Bob
Orders:
  - Order(id=3, user_id=2, product='Keyboard')
'''