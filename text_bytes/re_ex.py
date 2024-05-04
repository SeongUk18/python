import re

# 유니코드 문자열 예제
text = 'Hello, world! Привет, мир! こんにちは、世界！'
pattern = re.compile(r'\w+')

# 유니코드 문자열에서 단어 찾기
matches = pattern.findall(text)
print(matches)  # ['Hello', 'world', 'Привет', 'мир', 'こんにちは', '世界']

# 바이트 문자열 예제
byte_text = b'Hello, world! \xfa\xfb\xfc'
pattern = re.compile(rb'\w+')

# 바이트 문자열에서 단어 찾기
matches = pattern.findall(byte_text)
print(matches)  # [b'Hello', b'world']