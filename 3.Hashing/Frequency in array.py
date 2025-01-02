#You are given an array arr[] containing positive integers. The elements in the array arr[] range from 1 to n 
# (where n is the size of the array), and some numbers may be repeated or absent. Your task is to count the frequency of all 
# numbers in the range 1 to n and return an array of size n such that result[i] represents the frequency of the number i (1-based indexing).
n=int(input("Number :"))
arr=[0]*n
for i in range(n):
    arr[i]=int(input("Number :"))
l=[0 for i in range(len(arr))]
for i in arr:
    if i==0:
        continue
    l[i-1]+=1
print(l)
