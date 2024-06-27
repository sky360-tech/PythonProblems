def sum_digits(n):
    return sum(int(digit) for digit in str(n))

# Test cases
print(sum_digits(12345))  # 15
print(sum_digits(999))  # 27
print(sum_digits(0))  # 0
