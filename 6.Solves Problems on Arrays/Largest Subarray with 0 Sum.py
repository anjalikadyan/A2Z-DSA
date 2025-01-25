n=int(input("Enter a number: "))
nums=[0]*n
for i in range(n):
    nums[i]=int(input("enter number of array: "))
def maxLen( arr):
    sum_map = {}
    max_length = 0
    cumulative_sum = 0
    for i in range(len(arr)):
        cumulative_sum += arr[i]
        if cumulative_sum == 0:
            max_length = i + 1
        
        if cumulative_sum in sum_map:
            max_length = max(max_length, i - sum_map[cumulative_sum])
        else:
            sum_map[cumulative_sum] = i    
    return max_length
print(maxLen(nums))