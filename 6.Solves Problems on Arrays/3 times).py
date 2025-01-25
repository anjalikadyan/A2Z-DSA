from collections import Counter
n=int(input("Enter a number: "))
nums=[0]*n
for i in range(n):
    nums[i]=int(input("enter number of array: "))
def majorityElement( nums): 
    fre=Counter(nums)
    le=set()
    n=len(nums)
    for i in range(n):
        if fre[nums[i]]>(n/3):
            le.add(nums[i])
    de=list(le)
    return de
de=majorityElement(nums)
print(de)