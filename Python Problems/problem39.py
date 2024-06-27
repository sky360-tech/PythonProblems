def is_palindrome_number(n):
    s = str(n)
    return s == s[::-1]

# Test cases
print(is_palindrome_number(121))  # True
print(is_palindrome_number(123))  # False
print(is_palindrome_number(0))    # True
