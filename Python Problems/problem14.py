def count_within_range(lst, min_val, max_val):
    return len([x for x in lst if min_val <= x <= max_val])

# Test cases
print(count_within_range([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 40, 80))  # 5
print(count_within_range([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 15, 75))  # 6
print(count_within_range([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 25, 65))  # 4
