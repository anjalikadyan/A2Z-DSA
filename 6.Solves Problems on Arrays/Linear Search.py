n=int(input("Enter a number: "))
k=int(input("Enter a number: "))
arr=[0]*n
for i in range(len(arr)):
    if arr[i]==k:
        print(True)
    break
print(False)