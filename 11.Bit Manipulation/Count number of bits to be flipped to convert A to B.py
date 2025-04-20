def min_bit_flips(start: int, goal: int) -> int:
    # XOR will give a number where bits are 1 if they are different in start and goal
    xor_result = start ^ goal
    # Count the number of 1s in the binary representation of xor_result
    return bin(xor_result).count('1')

# Example usage:
start = 7
goal = 10
print(min_bit_flips(start, goal))  # Output: 3
