def stone_piles(n):
    return [n + 2 * i for i in range(n)]

# Test cases
print(stone_piles(2))  # [2, 4]
print(stone_piles(10))  # [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
print(stone_piles(3))  # [3, 5, 7]
print(stone_piles(17))  # [17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
