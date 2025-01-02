#The frequency of an element is the number of times it occurs in an array.You are given an integer array nums and an integer k.
#In one operation, you can choose an index of nums and increment the element at that index by 1.
#Return the maximum possible frequency of an element after performing at most k operations.
n=int(input("Number :"))
nums=[0]*n
for i in range(n):
    nums[i]=int(input("Number in array: "))
nums.sort()
k=int(input("K :"))
left=0
max_feq=0
total=0
for right in range(len(nums)):
    total+=nums[right]
    while(nums[right]*(right-left+1)>total+k):
        total-=nums[left]
        left+=1
    max_feq=max(max_feq,right-left+1)
print(max_feq)