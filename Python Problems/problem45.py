def diff_sum_product_digits(n):
    sum_digits = sum(int(digit) for digit in str(n))
    product_digits = 1
    for digit in str(n):
        product_digits *= int(digit)
    return sum_digits - product_digits

# Test cases
print(diff_sum_product_digits(12345))  # -105
print(diff_sum_product_digits(999))  # -702
print(diff_sum_product_digits(0))  # 0
