def sum_primes(n):
    primes = generate_primes(n)
    return sum(primes)

# Test cases
print(sum_primes(5))  # 28
print(sum_primes(10))  # 129
print(sum_primes(1))  # 2
