def all_unique_characters(s):
    return len(s) == len(set(s))

# Test cases
print(all_unique_characters("abcdef"))  # True
print(all_unique_characters("aabbcc"))  # False
print(all_unique_characters("123456"))  # True
