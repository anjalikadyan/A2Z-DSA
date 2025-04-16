def is_bit_set(num, i):
    return (num & (1 << i)) != 0

# Example usage
num = 10  # binary: 1010
i = 1

if is_bit_set(num, i):
    print(f"Bit {i} is set.")
else:
    print(f"Bit {i} is not set.")
