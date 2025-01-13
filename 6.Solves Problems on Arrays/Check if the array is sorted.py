n=int(input("Enter a number: "))
nums=[0]*n
for i in range(n):
    nums[i]=int(input("Enter a number in array: "))
count_breaks = 0
for i in range(n):
    if nums[i] > nums[(i + 1) % n]:
        count_breaks += 1
print(count_breaks <= 1)