def count_uppercase(s):
    return sum(1 for char in s if char.isupper())

# Test cases
print(count_uppercase("Hello World"))  # 2
print(count_uppercase("PYTHON"))  # 6
print(count_uppercase("javaScript"))  # 2
