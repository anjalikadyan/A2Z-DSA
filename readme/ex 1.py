# Code 1
a = 10
sum = 0
for i in range(a):
    sum += i
print(sum)

#Time Complexity: Big O(a).
#Space Complexity: Big O(1).

# Code 2
# Here c is a constant
for i in range(10):
    sum += i
print(sum)

#Time Complexity: Big O(1).
#Space Complexity: Big O(1).

# Code 3
# Here c is a positive integer constant
n=int(input())
for i in range(10):
    sum += i
print(sum)


for i in range(n):
    sum += i
print(sum)

#Time Complexity: Big O(n).
#Space Complexity: Big O(1).
