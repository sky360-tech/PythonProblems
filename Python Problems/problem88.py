def product_digits(n):
    result = 1
    for digit in str(n):
        result *= int(digit)
    return result

# Test cases
print(product_digits(123))  # 6
print(product_digits(456))  # 120
print(product_digits(789))  # 504
