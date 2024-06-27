def sum_cubes_fibonacci(n):
    fibs = [0, 1]
    for _ in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return sum(x ** 3 for x in fibs[:n])

# Test cases
print(sum_cubes_fibonacci(5))  # 58
print(sum_cubes_fibonacci(10))  # 319770
print(sum_cubes_fibonacci(1))  # 0
