def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Test cases
print(is_power_of_two(16))  # True
print(is_power_of_two(18))  # False
print(is_power_of_two(1))  # True
