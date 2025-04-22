def subsets(nums):
    result = []

    def backtrack(start, path):
        result.append(path[:])  # Add the current subset to the result
        for i in range(start, len(nums)):
            path.append(nums[i])            # Choose
            backtrack(i + 1, path)          # Explore
            path.pop()                      # Un-choose

    backtrack(0, [])
    return result
nums = [1, 2, 3]
print(subsets(nums))
