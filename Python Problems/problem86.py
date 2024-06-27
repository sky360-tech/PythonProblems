def hamming_distance(x, y):
    return bin(x ^ y).count('1')

# Test cases
print(hamming_distance(1, 4))  # 2
print(hamming_distance(3, 1))  # 1
print(hamming_distance(0, 255))  # 8
