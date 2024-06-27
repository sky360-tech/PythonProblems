def smallest_number(nums):
    nums = map(str, nums)
    nums_sorted = sorted(nums, key=cmp_to_key(lambda x, y: int(x + y) - int(y + x)))
    smallest = ''.join(nums_sorted)
    return smallest if smallest[0] != '0' else '0'

# Test cases
print(smallest_number([10, 2]))  # "102"
print(smallest_number([3, 30, 34, 5, 9]))  # "3033459"
print(smallest_number([0, 0]))  # "0"
