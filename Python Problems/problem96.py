def tribonacci(n):
    tribs = [0, 1, 1]
    for _ in range(3, n + 1):
        tribs.append(tribs[-1] + tribs[-2] + tribs[-3])
    return tribs[n]

# Test cases
print(tribonacci(4))  # 4
print(tribonacci(10))  # 149
print(tribonacci(0))  # 0
