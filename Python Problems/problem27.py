def second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2] if len(unique_lst) >= 2 else None

# Test cases
print(second_largest([1, 2, 3, 4, 5]))  # 4
print(second_largest([10, 10, 20, 20]))  # 10
print(second_largest([1]))  # None
