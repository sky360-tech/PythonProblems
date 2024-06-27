def sum_of_even(lst):
    return sum(x for x in lst if x % 2 == 0)

# Test cases
print(sum_of_even([1, 2, 3, 4, 5, 6]))  # 12
print(sum_of_even([10, 15, 20, 25, 30]))  # 60
print(sum_of_even([1, 3, 5, 7]))  # 0
