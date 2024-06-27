from itertools import combinations

def all_combinations(lst):
    comb_list = []
    for r in range(1, len(lst) + 1):
        comb_list.extend(combinations(lst, r))
    return comb_list

# Test cases
print(all_combinations([1, 2, 3]))  # [(1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
print(all_combinations([1]))  # [(1,)]
print(all_combinations([]))  # []
from itertools import combinations

def all_combinations(lst):
    comb_list = []
    for r in range(1, len(lst) + 1):
        comb_list.extend(combinations(lst, r))
    return comb_list

# Test cases
print(all_combinations([1, 2, 3]))  # [(1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
print(all_combinations([1]))  # [(1,)]
print(all_combinations([]))  # []
