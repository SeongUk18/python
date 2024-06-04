import itertools

for num in itertools.count(10, 2):
    if num > 20:
        break
    print(num)  # 10, 12, 14, 16, 18, 20

for i, item in enumerate(itertools.cycle(['A', 'B', 'C'])):
    if i >= 9:
        break
    print(item)  # A B C A B C A B C

for item in itertools.repeat('Hello', 3):
    print(item)  # Hello Hello Hello

for item in itertools.chain([1, 2, 3], ['a', 'b', 'c']):
    print(item)  # 1 2 3 a b c

data = ['A', 'B', 'C', 'D']
selectors = [1, 0, 1, 0]
for item in itertools.compress(data, selectors):
    print(item)  # A C

for item in itertools.dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]):
    print(item)  # 6 4 1

for item in itertools.takewhile(lambda x: x < 5, [1, 4, 6, 4, 1]):
    print(item)  # 1 4

for item in itertools.islice(range(10), 1, 8, 2):
    print(item)  # 1 3 5 7

for item in itertools.starmap(pow, [(2, 5), (3, 2), (10, 3)]):
    print(item)  # 32 9 1000

for item in itertools.product('AB', '12'):
    print(item)  # ('A', '1') ('A', '2') ('B', '1') ('B', '2')

for item in itertools.permutations('ABC', 2):
    print(item)  # ('A', 'B') ('A', 'C') ('B', 'A') ('B', 'C') ('C', 'A') ('C', 'B')

for item in itertools.combinations('ABC', 2):
    print(item)  # ('A', 'B') ('A', 'C') ('B', 'C')

for item in itertools.combinations_with_replacement('ABC', 2):
    print(item)  # ('A', 'A') ('A', 'B') ('A', 'C') ('B', 'B') ('B', 'C') ('C', 'C')

