data = bytearray(b"hello world")
mv = memoryview(data)

# 메모리 뷰를 사용하여 데이터 변경
mv[6:11] = b"WORLD"

print(data)  # bytearray(b'hello WORLD')
# mv를 통해 데이터의 일부를 "WORLD"로 변경하면, data의 내용도 업데이트되어 바뀐 내용을 반영