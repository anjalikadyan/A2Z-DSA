def count_distinct_subsequences(s):
    n = len(s)
    MOD = 10**9 + 7  # Optional: If you want to keep result within bounds
    
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: empty subsequence

    last_seen = {}  # Store the last index of each character

    for i in range(1, n + 1):
        char = s[i - 1]
        dp[i] = 2 * dp[i - 1]

        if char in last_seen:
            j = last_seen[char]
            dp[i] -= dp[j - 1]

        last_seen[char] = i

    return dp[n] - 1  # Exclude the empty subsequence

def more_distinct_subsequences(s1, s2):
    count1 = count_distinct_subsequences(s1)
    count2 = count_distinct_subsequences(s2)

    if count1 >= count2:
        return s1
    else:
        return s2
s1 = "abc"
s2 = "aaa"
print(more_distinct_subsequences(s1, s2))  # Output: "abc"
