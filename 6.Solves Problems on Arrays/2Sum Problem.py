n=int(input("Enter a number: "))
target=int(input("Enter a number: "))
nums=[0]*n
for i in range(n):
    nums[i]=int(input("enter number of array: "))
s=0
le=[]
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        elif nums[i]+nums[j]==target:
            le.append(i)
            le.append(j)
            break
    if len(le)==2:
        break
print(le)