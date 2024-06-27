def sum_squares_digits(n):
    return sum(int(digit) ** 2 for digit in str(n))

# Test cases
print(sum_squares_digits(123))  # 14
print(sum_squares_digits(456))  # 77
print(sum_squares_digits(789))  # 194
