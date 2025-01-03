n=int(input("Enter a number: "))
arr=[]
for i in range(n):
    arr.append(int(input("number in array: ")))
def merge(arr,l,m,r):
    left=l
    right=m+1
    re=[]
    while left<=m and right<=r:
        if arr[left]<=arr[right]:
            re.append(arr[left])
            left+=1
        else:
            re.append(arr[right])
            right+=1
    while left<=m:
        re.append(arr[left])
        left+=1
    while right<=r:
        re.append(arr[right])
        right+=1
    for i in range(len(re)):
        arr[l+i]=re[i]
def mergesort(arr,l,r):
    if l<r:
        m=(l+r)//2
        mergesort(arr,l,m)
        mergesort(arr,m+1,r)
        merge(arr,l,m,r)
mergesort(arr,0,len(arr)-1)
print(arr)
