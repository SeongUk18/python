import re


class WordIterable:
    def __init__(self, text):
        self.text = text

    def __iter__(self):
        for match in re.finditer(r'\b\w+\b', self.text):
            yield match.group()


# Example usage
text = "This is a sample text with several words."
word_iterable = WordIterable(text)
for word in word_iterable:
    print(word)
    