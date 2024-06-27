def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test cases
print(is_prime(29))  # True
print(is_prime(15))  # False
print(is_prime(2))   # True
print(is_prime(1))   # False
