def check_occurrences(lst):
    return lst.count(19) == 2 and lst.count(5) >= 3

# Test cases
print(check_occurrences([19, 19, 15, 5, 3, 5, 5, 2]))  # True
print(check_occurrences([19, 15, 15, 5, 3, 3, 5, 2]))  # False
print(check_occurrences([19, 19, 5, 5, 5, 5, 5]))  # True
