def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Test cases
print(lcm(4, 6))  # 12
print(lcm(21, 6))  # 42
print(lcm(101, 103))  # 10403
