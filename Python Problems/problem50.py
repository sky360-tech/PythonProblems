def longest_increasing_subsequence(lst):
    if not lst:
        return 0
    dp = [1] * len(lst)
    for i in range(1, len(lst)):
        for j in range(i):
            if lst[i] > lst[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# Test cases
print(longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]))  # 6
print(longest_increasing_subsequence([3, 10, 2, 1, 20]))  # 3
print(longest_increasing_subsequence([3, 2]))  # 1
