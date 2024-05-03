import codecs

# UTF-8로 텍스트 인코딩
text = "안녕하세요"
utf8_encoded = codecs.encode(text, 'utf-8')

# UTF-8로 디코딩
utf8_decoded = codecs.decode(utf8_encoded, 'utf-8')
