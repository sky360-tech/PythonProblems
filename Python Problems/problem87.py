def sum_digits(n):
    return sum(int(digit) for digit in str(n))

# Test cases
print(sum_digits(123))  # 6
print(sum_digits(456))  # 15
print(sum_digits(789))  # 24
 