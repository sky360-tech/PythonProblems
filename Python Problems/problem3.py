def check_integer(n):
    return n > 4**4 and n % 34 == 4

# Test cases
print(check_integer(922))  # True
print(check_integer(914))  # False
print(check_integer(854))  # True
