def is_pangram(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet <= set(s.lower())

# Test cases
print(is_pangram("The quick brown fox jumps over the lazy dog"))  # True
print(is_pangram("Hello World"))  # False
print(is_pangram("Pack my box with five dozen liquor jugs"))  # True
