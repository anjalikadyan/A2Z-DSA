n=int(input("Enter a number: "))
target=int(input("Enter a number: "))
nums=[0]*n
for i in range(n):
    nums[i]=int(input("Enter a number in array: "))
def add(nums,target):
    nums.sort()
    b=0
    for i in range(len(nums)):
        if nums[i]==target:
            return i
        if nums[i]>target:
            return i
    return len(nums)
print(add(nums,target))