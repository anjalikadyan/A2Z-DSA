def count_subsets_with_sum(arr, target):
    n = len(arr)
    
    dp = [[0] * (target + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(target + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][target]

arr = [2, 3, 5, 6, 8, 10]
target = 10
print("Number of subsets with sum", target, ":", count_subsets_with_sum(arr, target))
