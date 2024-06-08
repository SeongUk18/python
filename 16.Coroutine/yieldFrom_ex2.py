class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children is not None else []


def traverse_tree(node):
    yield node.value
    for child in node.children:
        yield from traverse_tree(child)


# 트리 구조 생성
tree = Node(1, [
    Node(2, [
        Node(4),
        Node(5)
    ]),
    Node(3, [
        Node(6),
        Node(7)
    ])
])

# 트리 순회
for value in traverse_tree(tree):
    print(value)

'''
1
2
4
5
3
6
7
'''
