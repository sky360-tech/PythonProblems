def separate_even_odd(lst):
    even = [x for x in lst if x % 2 == 0]
    odd = [x for x in lst if x % 2 != 0]
    return even, odd

# Test cases
print(separate_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # ([2, 4, 6, 8], [1, 3, 5, 7, 9])
print(separate_even_odd([1, 3, 5, 7]))  # ([], [1, 3, 5, 7])
print(separate_even_odd([2, 4, 6, 8]))  # ([2, 4, 6, 8], [])
