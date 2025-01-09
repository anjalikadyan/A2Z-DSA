n=9
# arr=[[0 for i in range(9)] for j in range(9)]
arr=[[3,7,3,7,7,3,7,3,7],[1,5,2,1,5,2,1,5,2],[4,6,8,4,6,8,4,6,8],[7,3,7,3,7,3,7,3,7],[2,1,5,2,1,5,2,1,5],[8,4,6,8,4,6,8,4,6],[5,2,1,5,2,1,5,2,1],[6,8,4,6,8,4,6,8,4],[9,9,9,9,9,9,9,9,9]]
#taking input from user for array(1-9)
# for i in range(n):
#     for j in range(n):
#         arr[i][j]=int(input("Enter the number: "))
#         if arr[i][j] not in range(1,10):
#             print("invalid number")
#             print("enter the number again")
#             arr[i][j]=int(input("Enter the number: "))
    # checking duplicate number in array
def check_duplicate(arr,k):
    count=0
    for i in arr:
        if i==k:
            count+=1
    return count
def check_dup(arr,k,j):
    count=0
    for i in range(n):
        if arr[i][j]==k:
            count+=1
    return count

#converting duplicate number to 0
for i in range(n):
    for j in range(n):
        fre=check_duplicate(arr[i],arr[i][j])
        fre1=check_dup(arr,arr[i][j],j)
        if fre>1:
            arr[i][j]=0
        if fre1>1:
            arr[i][j]=0
#checking missing number in array

def check(arr,arr1,j):
    arr4=[]
    for i in range(n):
        arr4.append(arr1[i][j])
    for i in range(1,10):
        if i not in arr and i not in arr4:
            return i
#converting 0 to missing number
def zero(arr):
    re=0
    for i in range(n):
        for j in range(n):
            if arr[i][j]==0:
                re=check(arr[i],arr,j)
                arr[i][j]=re
    return arr
for i in range(9):
    print(arr[i],end="\n")
ans=zero(arr)
for i in range(9):
    print(ans[i],end="\n")
