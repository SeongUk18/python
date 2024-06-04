import re

class WordIterator:
    def __init__(self, text):
        self.words = re.findall(r'\b\w+\b', text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return f"WordIterator({self.words})"


# Example usage
text = "This is a sample text with several words."
word_iterator = WordIterator(text)
print(len(word_iterator))  # 8
print(word_iterator)  # WordIterator(['This', 'is', 'a', 'sample', 'text', 'with', 'several', 'words'])
for i in range(len(word_iterator)):
    print(word_iterator[i])

'''
This
is
a
sample
text
with
several
words
'''