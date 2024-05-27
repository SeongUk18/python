import os

# 현재 디렉터리의 파일 목록을 str 타입으로 가져오기
entries_str = os.listdir('.')
print(entries_str)

# 현재 디렉터리를 bytes 타입으로 가져오기
entries_bytes = os.listdir(b'.')
print(entries_bytes)