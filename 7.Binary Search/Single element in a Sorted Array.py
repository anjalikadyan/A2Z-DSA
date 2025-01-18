from collections import Counter
n=int(input("Enter a number: "))
target=int(input("Enter a number: "))
nums=[0]*n
for i in range(n):
    nums[i]=int(input("Enter a number in array: "))
fre=Counter(nums)
for i in nums:
    if fre[i]==1:
        print(i)
print(-1)