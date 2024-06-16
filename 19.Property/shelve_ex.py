import shelve

# 데이터 저장
with shelve.open('my_shelve.db') as db:
    db['name'] = 'Alice'
    db['age'] = 30
    db['hobbies'] = ['reading', 'chess']

# 데이터 불러오기
with shelve.open('my_shelve.db') as db:
    print(db['name'])  # 출력: Alice
    print(db['age'])   # 출력: 30
    print(db['hobbies'])  # 출력: ['reading', 'chess']
