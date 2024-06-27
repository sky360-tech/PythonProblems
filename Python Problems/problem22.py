def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Test cases
print(is_leap_year(2020))  # True
print(is_leap_year(2021))  # False
print(is_leap_year(2000))  # True
print(is_leap_year(1900))  # False
