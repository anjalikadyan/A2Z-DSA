def unset_rightmost_set_bit(n):
    return n & (n - 1)

# Example usage
num = int(input("Enter a number: "))
result = unset_rightmost_set_bit(num)
print(f"After unsetting rightmost set bit: {bin(result)} ({result})")
