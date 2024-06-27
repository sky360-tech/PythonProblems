def check_length_and_fifth(lst):
    return len(lst) == 8 and lst.count(lst[4]) == 3

# Test cases
print(check_length_and_fifth([19, 19, 15, 5, 5, 5, 1, 2]))  # True
print(check_length_and_fifth([19, 15, 5, 7, 5, 5, 2]))  # False
print(check_length_and_fifth([11, 12, 14, 13, 14, 13, 15, 14]))  # True
print(check_length_and_fifth([19, 15, 11, 7, 5, 6, 2]))  # False
