class CharacterStyle:
    def __init__(self, font, size, bold):
        self.font = font
        self.size = size
        self.bold = bold

class CharacterStyleFactory:
    _styles = {}

    @classmethod
    def get_style(cls, font, size, bold):
        # 스타일 식별을 위한 키 생성
        key = (font, size, bold)
        if key not in cls._styles:
            cls._styles[key] = CharacterStyle(font, size, bold)
        return cls._styles[key]

class Character:
    def __init__(self, char, font, size, bold):
        self.char = char
        self.style = CharacterStyleFactory.get_style(font, size, bold)

# 클라이언트 코드
char_a = Character('A', 'Arial', 12, False)
char_b = Character('A', 'Arial', 12, False)
print(char_a.style == char_b.style)  # True, 같은 스타일 객체를 공유