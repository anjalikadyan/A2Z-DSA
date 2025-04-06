def combination_sum3(k, n):
    result = []

    def backtrack(start, path, remaining):
        if len(path) == k and remaining == 0:
            result.append(path[:])
            return
        if len(path) > k or remaining < 0:
            return
        
        for i in range(start, 10):  # Numbers from 1 to 9
            path.append(i)
            backtrack(i + 1, path, remaining - i)
            path.pop()

    backtrack(1, [], n)
    return result
print(combination_sum3(3, 7))  # Output: [[1, 2, 4]]
print(combination_sum3(3, 9))  # Output: [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
