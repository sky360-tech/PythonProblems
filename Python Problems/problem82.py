from functools import cmp_to_key

def largest_number(nums):
    nums = map(str, nums)
    nums_sorted = sorted(nums, key=cmp_to_key(lambda x, y: int(y + x) - int(x + y)))
    largest = ''.join(nums_sorted)
    return largest if largest[0] != '0' else '0'

# Test cases
print(largest_number([10, 2]))  # "210"
print(largest_number([3, 30, 34, 5, 9]))  # "9534330"
print(largest_number([0, 0]))  # "0"
