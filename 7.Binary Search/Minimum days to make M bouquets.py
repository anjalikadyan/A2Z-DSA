n=int(input("number: "))
k=int(input("number: "))
m=int(input("number: "))
bloomDay=[0]*n
for i in range(n):
    bloomDay[i]=int(input("array number: "))
def canMakeBouquets(mid):
    count = 0
    flowers = 0    
    for bloom in bloomDay:
        if bloom <= mid:
            flowers += 1
            if flowers == k:
                count += 1
                flowers = 0
        else:
            flowers = 0    
    print(count >= m)    
if len(bloomDay) < m * k:
    print(-1)   
left, right = min(bloomDay), max(bloomDay)    
while left < right:
    mid = (left + right) // 2
    if canMakeBouquets(mid):
        right = mid
    else:
        left = mid + 1    
print(left)