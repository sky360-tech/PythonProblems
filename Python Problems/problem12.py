def high_low(s):
    return max(s), min(s)

# Test cases
print(high_low({1, 2, 3, 4, 5}))  # (5, 1)
print(high_low({-10, 100, 200, 1}))  # (200, -10)
print(high_low({0}))  # (0, 0)
