def is_perfect_square(n):
    return int(n ** 0.5) ** 2 == n

# Test cases
print(is_perfect_square(25))  # True
print(is_perfect_square(26))  # False
print(is_perfect_square(0))   # True
