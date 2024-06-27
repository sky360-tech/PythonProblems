import re

def is_valid_palindrome(s):
    s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return s == s[::-1]

# Test cases
print(is_valid_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_valid_palindrome("race a car"))  # False
print(is_valid_palindrome(""))  # True
