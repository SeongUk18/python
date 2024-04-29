# 체이닝 예제
hashtable = [[] for _ in range(10)]  # 10개의 버킷을 가진 해시 테이블
def hash_function(key):
    return key % 10
def insert(hashtable, key, value):
    hash_key = hash_function(key)
    hashtable[hash_key].append((key, value))


# 선형 조사 예제
def insert(hashtable, key, value):
    original_hash = hash_key = hash_function(key)
    while hashtable[hash_key] is not None:
        hash_key = (original_hash + 1) % len(hashtable)
        if hash_key == original_hash:
            raise Exception("Hashtable is full")
    hashtable[hash_key] = (key, value)