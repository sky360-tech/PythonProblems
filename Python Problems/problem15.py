def reverse_if_multiple_of_four(s):
    return s[::-1] if len(s) % 4 == 0 else s

# Test cases
print(reverse_if_multiple_of_four("abcd"))  # dcba
print(reverse_if_multiple_of_four("abcde"))  # abcde
print(reverse_if_multiple_of_four("abcdefgh"))  # hgfedcba
