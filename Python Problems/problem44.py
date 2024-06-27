def product_digits(n):
    product = 1
    for digit in str(n):
        product *= int(digit)
    return product

# Test cases
print(product_digits(12345))  # 120
print(product_digits(999))  # 729
print(product_digits(0))  # 0
