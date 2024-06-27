from collections import Counter

def find_mode(lst):
    if not lst:
        return None
    data = Counter(lst)
    return max(data, key=data.get)

# Test cases
print(find_mode([1, 2, 2, 3, 4, 4, 4, 5]))  # 4
print(find_mode([1, 1, 2, 2, 3]))  # 1
print(find_mode([]))  # None
