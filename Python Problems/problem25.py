def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[:n]

# Test cases
print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(fibonacci(5))   # [0, 1, 1, 2, 3]
print(fibonacci(1))   # [0]
