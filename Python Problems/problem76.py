def is_palindrome_number(n):
    return str(n) == str(n)[::-1]

# Test cases
print(is_palindrome_number(121))  # True
print(is_palindrome_number(123))  # False
print(is_palindrome_number(12321))  # True
