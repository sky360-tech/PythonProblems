def max_product(lst):
    max_prod = float('-inf')
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            max_prod = max(max_prod, lst[i] * lst[j])
    return max_prod

# Test cases
print(max_product([1, 2, 3, 4]))  # 12
print(max_product([10, 10, 10]))  # 100
print(max_product([-1, -2, -3]))  # 6
