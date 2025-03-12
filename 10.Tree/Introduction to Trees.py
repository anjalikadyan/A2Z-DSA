n=int(input("enter a number: "))
def countNodes(i):
        sum=1
        j=0
        while (j<(i-1)):
            sum*=2
            j+=1
        return sum
print(countNodes(n))