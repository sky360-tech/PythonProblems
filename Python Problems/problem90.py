def is_perfect_square(n):
    return int(n ** 0.5) ** 2 == n

# Test cases
print(is_perfect_square(16))  # True
print(is_perfect_square(15))  # False
print(is_perfect_square(1))  # True
