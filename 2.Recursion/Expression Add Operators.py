from typing import List

def addOperators(num: str, target: int) -> List[str]:
    result = []

    def backtrack(index: int, path: str, value: int, prev: int):
        if index == len(num):
            if value == target:
                result.append(path)
            return
        
        for i in range(index, len(num)):
            # Skip numbers with leading zeros
            if i != index and num[index] == '0':
                break
            
            curr_str = num[index:i+1]
            curr = int(curr_str)

            if index == 0:
                # First number, pick it without any operator
                backtrack(i + 1, curr_str, curr, curr)
            else:
                backtrack(i + 1, path + '+' + curr_str, value + curr, curr)
                backtrack(i + 1, path + '-' + curr_str, value - curr, -curr)
                # For multiplication, subtract the previous value and add the result of multiplication
                backtrack(i + 1, path + '*' + curr_str, value - prev + (prev * curr), prev * curr)

    backtrack(0, '', 0, 0)
    return result
print(addOperators("123", 6))   # Output: ["1+2+3", "1*2*3"]
print(addOperators("232", 8))   # Output: ["2*3+2", "2+3*2"]
print(addOperators("105", 5))   # Output: ["1*0+5", "10-5"]
