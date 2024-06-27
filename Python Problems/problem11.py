def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Test cases
print(sum_of_digits(12345))  # 15
print(sum_of_digits(9999))  # 36
print(sum_of_digits(1001))  # 2
