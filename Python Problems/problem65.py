def is_valid_hexadecimal(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False

# Test cases
print(is_valid_hexadecimal("a"))  # True
print(is_valid_hexadecimal("g"))  # False
print(is_valid_hexadecimal("ff"))  # True
