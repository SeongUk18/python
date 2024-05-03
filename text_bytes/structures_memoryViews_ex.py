import struct

# 정수 1과 실수 2.3을 패킹
packed_data = struct.pack('if', 1, 2.3)

# 패킹된 데이터 언패킹
unpacked_data = struct.unpack('if', packed_data)

# Memory Views
# bytearray의 메모리 뷰 생성
data = bytearray('abcd', 'utf-8')
mv = memoryview(data)

# 메모리 뷰를 사용한 데이터 수정
mv[1] = ord('e')
