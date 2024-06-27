def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

# Test cases
print(count_vowels("Hello World"))  # 3
print(count_vowels("Python"))  # 1
print(count_vowels("AEIOUaeiou"))  # 10
