def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

# Test cases
print(intersection([1, 2, 3], [3, 4, 5]))  # [3]
print(intersection([1, 1, 2, 2], [2, 2, 3, 3]))  # [2]
print(intersection([1, 2, 3], [4, 5, 6]))  # []
