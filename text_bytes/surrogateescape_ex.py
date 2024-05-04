import os

# 파일 이름에 인코딩할 수 없는 바이트 포함
file_name = os.fsencode('example.txt') + b'\xff'

# 파일 생성
with open(file_name, 'w', encoding='utf-8', errors='surrogateescape') as f:
    f.write("Hello, world!")

# 파일 이름 읽기
for entry in os.listdir(b'.'):
    print(entry)  # 바이트로 출력

    # 파일 이름을 str로 변환
    decoded_name = entry.decode('utf-8', 'surrogateescape')
    print(decoded_name)  # surrogateescape를 사용하여 디코드

    # 다시 바이트로 인코딩하여 원래 파일 이름으로 복원
    re_encoded = decoded_name.encode('utf-8', 'surrogateescape')
    print(re_encoded)  # 원래 바이트 시퀀스로 복원


# 깨진 문자 처리 과정
# 파일 시스템에서 바이트 시퀀스로 파일 이름 읽기
file_name_bytes = os.fsencode('example.txt') + b'\xff'

# 파일 생성 (디코딩 에러를 회피하기 위해 surrogateescape 사용)
with open(file_name_bytes, 'w', encoding='utf-8', errors='surrogateescape') as f:
    f.write("Hello, world!")

# 파일 이름을 다시 읽고, 유니코드 문자열로 변환
for entry in os.listdir(b'.'):
    decoded_name = entry.decode('utf-8', 'surrogateescape')

    # 유니코드 문자열을 다시 원본 바이트로 인코딩
    re_encoded = decoded_name.encode('utf-8', 'surrogateescape')
    print(re_encoded)