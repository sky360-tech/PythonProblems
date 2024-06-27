def remove_duplicates(lst):
    return list(set(lst))

# Test cases
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # [1, 2, 3, 4, 5]
print(remove_duplicates([10, 10, 10]))  # [10]
print(remove_duplicates([]))  # []
