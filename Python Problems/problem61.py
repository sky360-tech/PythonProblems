def decimal_to_binary(n):
    return bin(n)[2:]

# Test cases
print(decimal_to_binary(10))  # "1010"
print(decimal_to_binary(255))  # "11111111"
print(decimal_to_binary(0))  # "0"
