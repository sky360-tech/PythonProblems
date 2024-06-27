def longest_unique_substring(s):
    chars = set()
    l = 0
    longest = 0
    for r in range(len(s)):
        while s[r] in chars:
            chars.remove(s[l])
            l += 1
        chars.add(s[r])
        longest = max(longest, r - l + 1)
    return longest

# Test cases
print(longest_unique_substring("abcabcbb"))  # 3
print(longest_unique_substring("bbbbb"))  # 1
print(longest_unique_substring("pwwkew"))  # 3
