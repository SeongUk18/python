words = ['café', 'cable', 'cab']
sorted_words = sorted(words)
print(sorted_words)  # ['cab', 'café', 'cable']

from pyuca import Collator
collator = Collator()

words = ['café', 'cable', 'cab', 'cafe']
sorted_words = sorted(words, key=collator.sort_key)
print(sorted_words)  # ['cab', 'cafe', 'café', 'cable']
