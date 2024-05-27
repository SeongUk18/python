# 파일 입출력과 기본 인코딩
# 파일을 UTF-8 인코딩으로 명시적으로 열기
with open("file.txt", "r", encoding="utf-8") as file:
    content = file.read()

# 시스템 기본 인코딩 확인하기
import sys
print(sys.getdefaultencoding())  # 'utf-8' 출력될 가능성이 높음

# 파이썬에서 유니코드 정규화 사용하기
import unicodedata

# 원래 문자열
s1 = 'café'  # "é"가 하나의 문자
s2 = 'cafe\u0301'  # "e"와 "´"가 조합된 문자




