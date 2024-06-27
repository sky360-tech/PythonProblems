def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

# Test cases
print(largest_prime_factor(56))  # 7
print(largest_prime_factor(315))  # 7
print(largest_prime_factor(13))  # 13
