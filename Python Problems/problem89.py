def digital_root(n):
    while n >= 10:
        n = sum_digits(n)
    return n

# Test cases
print(digital_root(123))  # 6
print(digital_root(456))  # 6
print(digital_root(789))  # 6
