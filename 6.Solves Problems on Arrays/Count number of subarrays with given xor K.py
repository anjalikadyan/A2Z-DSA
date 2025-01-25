n=int(input("Enter a number: "))
nums=[0]*n
for i in range(n):
    nums[i]=int(input("enter number of array: "))
def find_missing_number_xor(arr):
    n = len(arr) + 1 
    xor_all = 0
    xor_arr = 0
    for i in range(1, n + 1):
        xor_all ^= i
    for num in arr:
        xor_arr ^= num
    return xor_all ^ xor_arr
print(find_missing_number_xor(nums))