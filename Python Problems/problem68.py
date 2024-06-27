def is_perfect_number(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

# Test cases
print(is_perfect_number(6))  # True
print(is_perfect_number(28))  # True
print(is_perfect_number(12))  # False
