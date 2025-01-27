n=int(input("Enter a number: "))
nums=[0]*n
for i in range(n):
    nums[i]=int(input("enter number of array: "))

def reversePairs(self, nums):
    def merge_and_count(start, mid, end):
        count = 0
        j = mid + 1
        for i in range(start, mid + 1):
            while j <= end and nums[i] > 2 * nums[j]:
                j += 1
            count += (j - mid - 1)
        temp = []
        i, j = start, mid + 1
        while i <= mid and j <= end:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1
        while i <= mid:
            temp.append(nums[i])
            i += 1
        while j <= end:
            temp.append(nums[j])
            j += 1
        for i in range(len(temp)):
            nums[start + i] = temp[i]
        return count

    def merge_sort_and_count(start, end):
        if start >= end:
            return 0
        mid = (start + end) // 2
        count = merge_sort_and_count(start, mid)
        count += merge_sort_and_count(mid + 1, end)
        count += merge_and_count(start, mid, end)
        return count
    return merge_sort_and_count(0, len(nums) - 1)
print(reversePairs(nums))