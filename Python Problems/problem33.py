def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

# Test cases
print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))  # False
print(is_anagram("triangle", "integral"))  # True
