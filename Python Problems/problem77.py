def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Test cases
print(gcd(48, 18))  # 6
print(gcd(56, 98))  # 14
print(gcd(101, 103))  # 1
