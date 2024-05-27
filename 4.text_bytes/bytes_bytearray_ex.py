b = bytes("안녕하세요", encoding='utf-8')

b = bytes([65, 66, 67])  # ASCII 값으로 'A', 'B', 'C'

b = bytes(10)  # 길이가 10인 0으로 채워진 바이트

ba = bytearray("안녕하세요", encoding='utf-8')

ba = bytearray([65, 66, 67])

ba = bytearray(10)


# 공통 메소드
b = bytes("hello world", 'utf-8')
count = b.count(b'l')  # b'l'의 개수

index = b.find(b'lo')  # 'lo'의 시작 인덱스

index = b.index(b'lo')

starts = b.startswith(b'he')  # True
ends = b.endswith(b'ld')  # True

parts = [b'Hello', b'World']
joined = b' '.join(parts)  # b'Hello World'

# bytearray 전용 메소드
ba = bytearray(b'hello')
ba.append(33)  # b'hello!'

ba.extend(b' world')

ba.insert(1, b'a')

last_byte = ba.pop()

ba.remove(b'l')

