import re


class WordIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.words):
            word = self.words[self.index]
            self.index += 1
            return word
        else:
            raise StopIteration


class WordIterable:
    def __init__(self, text):
        self.words = re.findall(r'\b\w+\b', text)

    def __iter__(self):
        return WordIterator(self.words)


# Example usage
text = "This is a sample text with several words."
word_iterable = WordIterable(text)
for word in word_iterable:
    print(word)

