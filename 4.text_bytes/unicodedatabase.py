import unicodedata

# 문자에 대한 정보 조회
char = 'A'
name = unicodedata.name(char)
category = unicodedata.category(char)
numeric_value = unicodedata.numeric('Ⅳ', None)
decimal_value = unicodedata.decimal('9', None)

print("Name:", name)  # 'LATIN CAPITAL LETTER A'
print("Category:", category)  # 'Lu' (Letter, Uppercase)
print("Numeric Value of Ⅳ:", numeric_value)  # 4
print("Decimal Value of 9:", decimal_value)  # 9
