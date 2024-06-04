import re


class WordIterable:
    def __init__(self, text):
        self.text = text

    def __iter__(self):
        return self.word_generator()

    def word_generator(self):
        words = re.findall(r'\b\w+\b', self.text)
        for word in words:
            yield word


# Example usage
text = "This is a sample text with several words."
word_iterable = WordIterable(text)
for word in word_iterable:
    print(word)

