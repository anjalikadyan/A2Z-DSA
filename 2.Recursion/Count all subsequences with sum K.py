def combinationSum(candidates, target):
    result = []

    def backtrack(start, current_combination, current_sum):
        if current_sum == target:
            result.append(current_combination[:])  # Found a valid combination
            return
        elif current_sum > target:
            return  # Exceeded the target, stop exploration

        for i in range(start, len(candidates)):
            current_combination.append(candidates[i])
            # We pass i, not i+1, because we can reuse the same element
            backtrack(i, current_combination, current_sum + candidates[i])
            current_combination.pop()  # Backtrack

    backtrack(0, [], 0)
    return result
candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))
