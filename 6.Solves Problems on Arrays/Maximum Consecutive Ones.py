n=int(input("Enter a number: "))
nums=[0]*n
a=0
b=0
for i in range(len(nums)):
    if nums[i]==1:
        a+=1
    else:
        a=0
    b=max(b,a)
print(b)