def is_happy_number(n):
    def get_next(num):
        return sum(int(digit) ** 2 for digit in str(num))
    slow = n
    fast = get_next(n)
    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
    return fast == 1

# Test cases
print(is_happy_number(19))  # True
print(is_happy_number(2))  # False
print(is_happy_number(1))  # True
