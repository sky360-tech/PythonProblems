from collections import Counter

def are_anagrams(s1, s2):
    return Counter(s1) == Counter(s2)

# Test cases
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))  # False
print(are_anagrams("triangle", "integral"))  # True
