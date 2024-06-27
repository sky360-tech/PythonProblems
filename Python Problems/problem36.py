def sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))

# Test cases
print(sum_of_squares(5))  # 55
print(sum_of_squares(10))  # 385
print(sum_of_squares(1))  # 1
