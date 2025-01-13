n=int(input("Enter a number: "))
k=int(input("Enter a number: "))
nums=[0]*n
for i in range(n):
    nums[i]=int(input("Enter a number in array: "))
k%=n
nums.reverse()
nums[k:]=reversed(nums[k:])
nums[:k]=reversed(nums[:k])