# 유니코드 정규화 사용하기
import unicodedata

# 원래 문자열
s1 = 'café'  # "é"가 하나의 문자
s2 = 'cafe\u0301'  # "e"와 "´"가 조합된 문자

# NFC 정규화: 조합된 형태
nfc1 = unicodedata.normalize('NFC', s1)
nfc2 = unicodedata.normalize('NFC', s2)
print(nfc1 == nfc2)  # True 출력

# NFD 정규화: 분해된 형태
nfd1 = unicodedata.normalize('NFD', s1)
nfd2 = unicodedata.normalize('NFD', s2)
print(nfd1 == nfd2)  # True 출력

# 호환성 분할
import unicodedata

text = 'The price is ① dollar.'
nfkd_text = unicodedata.normalize('NFKD', text)
nfkc_text = unicodedata.normalize('NFKC', text)

print('NFKD:', nfkd_text)  # The price is 1 dollar.
print('NFKC:', nfkc_text)  # The price is 1 dollar.

# 케이스 폴딩
# 케이스 폴딩 예제
str1 = "Fluß"
str2 = "FLUSS"

# 소문자 변환을 사용한 비교
lowercase_comparison = str1.lower() == str2.lower()  # True

# 케이스 폴딩을 사용한 비교
casefold_comparison = str1.casefold() == str2.casefold()  # True

print("Lowercase Comparison:", lowercase_comparison)
print("Casefold Comparison:", casefold_comparison)

# 유틸리티 함수
import unicodedata
import re


def normalize_text(input_text, remove_punctuation=True):
    # 유니코드 NFKC 정규화 수행
    normalized = unicodedata.normalize('NFKC', input_text)

    # 케이스 폴딩을 통해 대소문자 구분 제거
    normalized = normalized.casefold()

    # 필요한 경우 특수 문자 제거
    if remove_punctuation:
        normalized = re.sub(r'[^\w\s]', '', normalized)

    # 공백 정리
    normalized = re.sub(r'\s+', ' ', normalized).strip()

    return normalized


# 사용 예시
text1 = "Hello, World!"
text2 = "hello world"
normalized_text1 = normalize_text(text1)
normalized_text2 = normalize_text(text2)

print("Text 1:", normalized_text1)
print("Text 2:", normalized_text2)
print("Is Matched:", normalized_text1 == normalized_text2)

# 발음 구별 기호 제거
import unicodedata


def remove_diacritics(input_text):
    # NFKD 정규화를 사용하여 문자를 기본 문자와 다이어크리틱스로 분리
    normalized = unicodedata.normalize('NFKD', input_text)

    # 다이어크리틱스를 제거하고 기본 문자만 유지
    result = ''.join([c for c in normalized if not unicodedata.combining(c)])
    return result


# 예시 사용
text = "São Paulo, résumé, façade, naïve, coöperate"
cleaned_text = remove_diacritics(text)
print(cleaned_text)
