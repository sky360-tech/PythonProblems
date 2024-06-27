def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)

# Test cases
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]
print(merge_sorted_lists([1, 1, 1], [2, 2, 2]))  # [1, 1, 1, 2, 2, 2]
print(merge_sorted_lists([], [2, 3, 4]))  # [2, 3, 4]
