#For example 1:

def prime(a: int):
    sum = 0
    if(a > 0):
        sum = 12 + a  # Base case
    else:
        prime(a + 1)  # Recursive call