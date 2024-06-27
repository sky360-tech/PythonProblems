from itertools import permutations

def all_permutations(lst):
    return list(permutations(lst))

# Test cases
print(all_permutations([1, 2, 3]))  # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
print(all_permutations([1, 1, 2]))  # [(1, 1, 2), (1, 2, 1), (1, 1, 2), (1, 2, 1), (2, 1, 1), (2, 1, 1)]
print(all_permutations([1]))  # [(1,)]
