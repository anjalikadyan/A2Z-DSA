def subset_sums(arr):
    result = []

    def dfs(index, current_sum):
        if index == len(arr):
            result.append(current_sum)
            return
        # Include current element
        dfs(index + 1, current_sum + arr[index])
        # Exclude current element
        dfs(index + 1, current_sum)

    dfs(0, 0)
    return result
arr = [1, 2, 3]
print(subset_sums(arr))
