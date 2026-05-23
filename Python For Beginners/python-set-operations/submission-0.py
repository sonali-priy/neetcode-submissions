from typing import List

def count_unique_words(words: List[str]) -> int:
    if len(words) ==0:
        return 0
    unique_words = set(words)
    list_unique_words = list(unique_words)
    return len(list_unique_words)

# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
