def sum_of_three(x, y, z):
    return 0 if x == y or y == z or x == z else x + y + z

# Test cases
print(sum_of_three(1, 2, 3))  # 6
print(sum_of_three(3, 3, 3))  # 0
print(sum_of_three(1, 1, 2))  # 0
print(sum_of_three(1, 2, 2))  # 0
