from collections import deque

dq = deque([1, 2, 3, 4, 5])
dq.append(6)        # [1, 2, 3, 4, 5, 6]
dq.appendleft(0)     # [0, 1, 2, 3, 4, 5, 6]
dq.pop()             # [0, 1, 2, 3, 4, 5]
dq.popleft()         # [1, 2, 3, 4, 5]


import queue

# 일반적인 Queue
q = queue.Queue()
q.put(1)    # 큐에 1 추가
q.put(2)    # 큐에 2 추가
print(q.get())  # 1 출력
print(q.get())  # 2 출력

# LifoQueue 생성
lifo_queue = queue.LifoQueue()

# 요소 추가
lifo_queue.put('a')
lifo_queue.put('b')
lifo_queue.put('c')

# 요소 제거 및 출력
print(lifo_queue.get())  # 출력: c
print(lifo_queue.get())  # 출력: b
print(lifo_queue.get())  # 출력: a

# PriorityQueue 생성
priority_queue = queue.PriorityQueue()

# 요소 추가 (우선순위, 값)
priority_queue.put((2, 'level two'))
priority_queue.put((1, 'level one'))
priority_queue.put((3, 'level three'))

# 요소 제거 및 출력
print(priority_queue.get()[1])  # 출력: level one
print(priority_queue.get()[1])  # 출력: level two
print(priority_queue.get()[1])  # 출력: level three