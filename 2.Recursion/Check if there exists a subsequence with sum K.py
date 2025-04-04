def combinationSum2(candidates, target):
    candidates.sort()  # Sort to handle duplicates
    result = []

    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        if remaining < 0:
            return

        prev = -1  # Placeholder for duplicate check
        for i in range(start, len(candidates)):
            if candidates[i] == prev:
                continue  # Skip duplicates
            if candidates[i] > remaining:
                break  # No need to proceed further
            path.append(candidates[i])
            backtrack(i + 1, path, remaining - candidates[i])  # i + 1 to avoid reuse
            path.pop()
            prev = candidates[i]

    backtrack(0, [], target)
    return result
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(combinationSum2(candidates, target))
