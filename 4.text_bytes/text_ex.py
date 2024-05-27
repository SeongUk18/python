s = 'Hello'
first_char = s[0]  # 'H'

char = 'A'
lower_char = char.lower()  # 'a'

korean_char = '\uAC00'  # 한글 '가'

# 문자열을 UTF-8 바이트 시퀀스로 인코딩
text = "안녕하세요"
encoded_text = text.encode('utf-8')  # UTF-8로 인코딩
print(encoded_text)  # b'\xec\x95\x88\xeb\x85\x95\xed\x95\x98\xec\x84\xb8\xec\x9a\x94'

# 바이트 시퀀스를 다시 문자열로 디코딩
decoded_text = encoded_text.decode('utf-8')  # UTF-8로 디코딩
print(decoded_text)  # '안녕하세요'
