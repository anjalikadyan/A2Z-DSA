def wordBreak(s, wordDict):
    word_set = set(wordDict)  # For faster lookup
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string can always be segmented

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break  # No need to check further for this i

    return dp[n]
s = "leetcode"
wordDict = ["leet", "code"]
print(wordBreak(s, wordDict))  # Output: True
