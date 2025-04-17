def is_power_of_two(number):
    if number <= 0:
        return False
    return (number & (number - 1)) == 0

# Example usage
num = int(input("Enter a number: "))
if is_power_of_two(num):
    print(f"{num} is a power of 2.")
else:
    print(f"{num} is not a power of 2.")
