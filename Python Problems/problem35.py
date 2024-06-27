def longest_word(words):
    return max(words, key=len) if words else None

# Test cases
print(longest_word(["apple", "banana", "cherry"]))  # "banana"
print(longest_word(["a", "bb", "ccc"]))  # "ccc"
print(longest_word([]))  # None
