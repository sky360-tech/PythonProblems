def unique_substrings(s, length):
    return list(set(s[i:i+length] for i in range(len(s) - length + 1)))

# Test cases
print(unique_substrings("hello", 2))  # ['el', 'he', 'lo', 'll']
print(unique_substrings("banana", 3))  # ['ana', 'nan', 'ban']
print(unique_substrings("abc", 1))  # ['a', 'b', 'c']
