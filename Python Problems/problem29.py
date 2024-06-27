def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Test cases
print(gcd(48, 18))  # 6
print(gcd(100, 10))  # 10
print(gcd(17, 13))  # 1
