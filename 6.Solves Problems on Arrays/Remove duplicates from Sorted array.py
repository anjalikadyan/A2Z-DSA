n=int(input("Enter a number: "))
nums=[0]*n
for i in range(n):
    nums[i]=int(input("Enter a number in array: "))
if not nums:
    print("")
else:
    count=0
    for i in range(1,len(nums)):
        if nums[i]!=nums[count]:
            count+=1
            nums[count]=nums[i]
print(count+1)