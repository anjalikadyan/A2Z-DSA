def subsets_with_dup(nums):
    result = []
    nums.sort()  

    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result
nums = [1, 2, 2]
print(subsets_with_dup(nums))
