def union(lst1, lst2):
    return list(set(lst1) | set(lst2))

# Test cases
print(union([1, 2, 3], [3, 4, 5]))  # [1, 2, 3, 4, 5]
print(union([1, 1, 2, 2], [2, 2, 3, 3]))  # [1, 2, 3]
print(union([1, 2, 3], [4, 5, 6]))  # [1, 2, 3, 4, 5, 6]
