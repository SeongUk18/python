# UnicodeEncodeError 처리
text = "안녕하세요"
encoded_text = text.encode('ascii', errors='ignore')  # 무시
encoded_text = text.encode('ascii', errors='replace')  # �로 대체

# UnicodeDecodeError 처리
bytes_data = b'\xff\xfe\x00\x00'
decoded_data = bytes_data.decode('utf-16', errors='replace')

# 바이트 시퀀스의 인코딩 방식을 알아내는 방법
import chardet
raw_data = b'\xec\x95\x88\xeb\x85\x95'
result = chardet.detect(raw_data)
print(result['encoding'])  # utf-8

# BOM: 유용한 깨진 문자
with open('file.txt', encoding='utf-8-sig') as f:
    content = f.read()
