def is_valid_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Test cases
print(is_valid_number("123"))  # True
print(is_valid_number("123.456"))  # True
print(is_valid_number("abc"))  # False
