from math import comb

def catalan_number(n):
    return comb(2 * n, n) // (n + 1)

# Test cases
print(catalan_number(5))  # 42
print(catalan_number(10))  # 16796
print(catalan_number(0))  # 1
