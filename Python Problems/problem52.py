from collections import Counter

def first_non_repeating_character(s):
    counts = Counter(s)
    for char in s:
        if counts[char] == 1:
            return char
    return None

# Test cases
print(first_non_repeating_character("swiss"))  # 'w'
print(first_non_repeating_character("hello"))  # 'h'
print(first_non_repeating_character("aabbcc"))  # None
