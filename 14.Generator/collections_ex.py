from collections import deque

d = deque(maxlen=3)
for i in range(5):
    d.append(i)
    print(d)
'''
deque([0], maxlen=3)
deque([0, 1], maxlen=3)
deque([0, 1, 2], maxlen=3)
deque([1, 2, 3], maxlen=3)
deque([2, 3, 4], maxlen=3)
'''

from collections import defaultdict

d = defaultdict(int)
d['a'] += 1
print(d)
# defaultdict(<class 'int'>, {'a': 1})

from collections import OrderedDict

d = OrderedDict()
d['one'] = 1
d['two'] = 2
for key in d:
    print(key, d[key])
'''
one 1
two 2
'''

from collections import Counter

cnt = Counter('abracadabra')
print(cnt)
# Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})


from collections import ChainMap

dict1 = {'one': 1, 'two': 2}
dict2 = {'three': 3, 'four': 4}
chain = ChainMap(dict1, dict2)
print(chain)
# ChainMap({'one': 1, 'two': 2}, {'three': 3, 'four': 4})
