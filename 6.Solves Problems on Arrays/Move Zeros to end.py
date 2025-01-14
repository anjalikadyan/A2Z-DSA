n=int(input("Enter a number: "))
nums=[0]*n
j=0
for i in range(len(nums)):
    if nums[i]!=0:
        nums[j],nums[i]=nums[i],nums[j]
        j+=1
print(nums)
        