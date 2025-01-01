n=int(input("enter a number= "))
#this is a code for convert number to words
arr=["zero","one","two","three","four","five","six","seven","eight","nine"]
def num(n):
    if n==0:
        return ""
    else:
        d=n%10
        n=n//10
        num(n)
        print(arr[d],end=" ")
num(n)