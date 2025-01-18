n=int(input("Enter a number: "))
target=int(input("Enter a number: "))
nums=[0]*n
for i in range(n):
    nums[i]=int(input("Enter a number in array: "))
n=min(nums)
b=nums.index(n)
print(b)