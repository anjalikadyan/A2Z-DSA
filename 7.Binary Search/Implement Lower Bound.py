n=int(input("Enter a number: "))
target=int(input("Enter a number: "))
nums=[0]*n
for i in range(n):
    nums[i]=int(input("Enter a number in array: "))
a=0
b=-1
for i in range(len(nums)):
    if nums[i]<=target and nums[i]>a:
        a=nums[i]
        b=i
print(b)
            