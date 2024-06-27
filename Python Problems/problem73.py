def generate_primes(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        is_prime = all(candidate % prime != 0 for prime in primes)
        if is_prime:
            primes.append(candidate)
        candidate += 1
    return primes

# Test cases
print(generate_primes(5))  # [2, 3, 5, 7, 11]
print(generate_primes(10))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print(generate_primes(1))  # [2]
