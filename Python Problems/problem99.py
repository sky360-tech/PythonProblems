def pell_number(n):
    pells = [0, 1]
    for _ in range(2, n + 1):
        pells.append(2 * pells[-1] + pells[-2])
    return pells[n]

# Test cases
print(pell_number(5))  # 29
print(pell_number(10))  # 2378
print(pell_number(0))  # 0
