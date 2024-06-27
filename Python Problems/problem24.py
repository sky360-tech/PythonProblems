def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Test cases
print(factorial(5))  # 120
print(factorial(7))  # 5040
print(factorial(0))  # 1
