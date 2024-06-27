def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in s if char not in vowels)

# Test cases
print(remove_vowels("Hello World"))  # "Hll Wrld"
print(remove_vowels("Python"))  # "Pythn"
print(remove_vowels("AEIOUaeiou"))  # ""

