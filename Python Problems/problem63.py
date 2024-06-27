def decimal_to_hexadecimal(n):
    return hex(n)[2:]

# Test cases
print(decimal_to_hexadecimal(10))  # "a"
print(decimal_to_hexadecimal(255))  # "ff"
print(decimal_to_hexadecimal(0))  # "0"
