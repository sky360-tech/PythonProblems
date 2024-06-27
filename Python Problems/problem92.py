def sum_fibonacci(n):
    fibs = [0, 1]
    for _ in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return sum(fibs[:n])

# Test cases
print(sum_fibonacci(5))  # 7
print(sum_fibonacci(10))  # 88
print(sum_fibonacci(1))  # 0
