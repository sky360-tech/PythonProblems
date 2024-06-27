def even_numbers_up_to(n):
    return [x for x in range(2, n+1, 2)]

# Test cases
print(even_numbers_up_to(10))  # [2, 4, 6, 8, 10]
print(even_numbers_up_to(15))  # [2, 4, 6, 8, 10, 12, 14]
print(even_numbers_up_to(1))  # []
