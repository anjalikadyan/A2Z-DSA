def is_odd(number):
    if number % 2 != 0:
        return True
    else:
        return False

# Example usage
num = int(input("Enter a number: "))
if is_odd(num):
    print(f"{num} is an odd number.")
else:
    print(f"{num} is not an odd number.")
