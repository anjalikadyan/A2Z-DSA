n=int(input("Enter a number: "))
target=int(input("Enter a number: "))
nums=[0]*n
for i in range(n):
    nums[i]=int(input("Enter a number in array: "))
for i in range(len(nums)):
    if nums[i]==target:
        print(i)
print(-1)