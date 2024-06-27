def tetranacci(n):
    tets = [0, 0, 0, 1]
    for _ in range(4, n + 1):
        tets.append(tets[-1] + tets[-2] + tets[-3] + tets[-4])
    return tets[n]

# Test cases
print(tetranacci(5))  # 1
print(tetranacci(10))  # 35
print(tetranacci(0))  # 0
