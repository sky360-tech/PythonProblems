def sum_squares_fibonacci(n):
    fibs = [0, 1]
    for _ in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return sum(x ** 2 for x in fibs[:n])

# Test cases
print(sum_squares_fibonacci(5))  # 15
print(sum_squares_fibonacci(10))  # 4895
print(sum_squares_fibonacci(1))  # 0
