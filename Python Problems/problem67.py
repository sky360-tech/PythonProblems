def is_armstrong_number(n):
    num_str = str(n)
    power = len(num_str)
    return n == sum(int(digit) ** power for digit in num_str)

# Test cases
print(is_armstrong_number(153))  # True
print(is_armstrong_number(123))  # False
print(is_armstrong_number(9474))  # True
