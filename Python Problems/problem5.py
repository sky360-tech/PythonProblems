def check_substring(lst):
    return lst[-2] in lst[-1]

# Test cases
print(check_substring(['a', 'abb', 'sfs', 'oo', 'de', 'sfde']))  # True
print(check_substring(['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']))  # False
print(check_substring(['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew']))  # False
print(check_substring(['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']))  # True
