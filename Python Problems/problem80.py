def have_same_elements(lst1, lst2):
    return sorted(lst1) == sorted(lst2)

# Test cases
print(have_same_elements([1, 2, 3], [3, 2, 1]))  # True
print(have_same_elements([1, 2, 2], [2, 2, 1]))  # True
print(have_same_elements([1, 2, 3], [1, 2, 4]))  # False
