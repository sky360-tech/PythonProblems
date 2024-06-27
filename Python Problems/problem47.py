def reverse_words(s):
    return ' '.join(reversed(s.split()))

# Test cases
print(reverse_words("Hello World"))  # "World Hello"
print(reverse_words("Python is awesome"))  # "awesome is Python"
print(reverse_words(""))  # ""
