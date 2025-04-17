def count_set_bits(number):
    count = 0
    while number:
        count += number & 1
        number >>= 1
    return count

# Example usage
num = int(input("Enter a number: "))
print(f"Number of set bits in {num} is {count_set_bits(num)}.")
