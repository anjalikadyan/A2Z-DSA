
num="4206"
def largestOddNumber(self, num):
    n=len(num)
    a=0
    a1=0
    le=[]
    for i in range(n):
            # print(num[(n-1)-i])
        if int(num[(n-1)-i])%2!=0:
            a=(n-1)-i
            a1+=1
            print(num[(n-1)-i])
            break
    if a1==0:
        return ""
    for i in range(a+1):
        le.append(num[i])
    return ''.join(le)
print(largestOddNumber(num))