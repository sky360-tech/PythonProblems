def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

# Test cases
print(common_elements([1, 2, 3], [2, 3, 4]))  # [2, 3]
print(common_elements([1, 1, 1], [1, 2, 2]))  # [1]
print(common_elements([1, 2, 3], [4, 5, 6]))  # []
