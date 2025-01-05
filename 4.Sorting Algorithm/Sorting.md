# Sorting Algorithms for Arrays

## 1. Selection Sort
Selection Sort is a sorting algorithm that works by selecting the minimum element from the unsorted portion of the array and swapping it with the first element of the unsorted portion. This process is repeated, excluding the already sorted elements.

### Example:
Let’s consider an array:
`arr = [1, 4, 7, 3]`

**Steps:**
1. The first minimum element is `1`, which is already at the zeroth index.
2. The next minimum element is `3`, which is swapped with the element at the first index:
   `arr = [1, 3, 7, 4]`
3. The next minimum element is `4`, which is swapped with the element at the second index:
   `arr = [1, 3, 4, 7]`
4. The array is now sorted.

### Time Complexity:
- Worst case: **O(n^2)**
- Best case: **O(n^2)**
- Average case: **O(n^2)**

### Space Complexity:
- Auxiliary Space: **O(1)**

---

## 2. Bubble Sort
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. After each pass, the largest unsorted element bubbles up to its correct position. It is not suitable for large datasets due to its high time complexity.

### Example:
Let’s consider an array:
`arr = [5, 3, 8, 6, 2]`

**Steps:**
1. Compare `5` and `3`. Swap them: `arr = [3, 5, 8, 6, 2]`
2. Compare `5` and `8`. No swap: `arr = [3, 5, 8, 6, 2]`
3. Compare `8` and `6`. Swap them: `arr = [3, 5, 6, 8, 2]`
4. Compare `8` and `2`. Swap them: `arr = [3, 5, 6, 2, 8]`
5. Repeat for the remaining unsorted portion until the array becomes: `arr = [2, 3, 5, 6, 8]`

### Time Complexity:
- Worst case: **O(n^2)**
- Best case: **O(n)** (when the array is already sorted)
- Average case: **O(n^2)**

### Space Complexity:
- Auxiliary Space: **O(1)**

---

## 3. Insertion Sort
Insertion Sort is a simple sorting algorithm that builds the sorted array one element at a time. It works by iteratively taking an element from the unsorted portion of the array and inserting it into its correct position in the sorted portion.

### Example:
Let’s consider an array:
`arr = [7, 4, 5, 2]`

**Steps:**
1. Start with the second element `4`. Insert it into the correct position in the sorted portion:
   `arr = [4, 7, 5, 2]`
2. Take the next element `5`. Insert it into the correct position:
   `arr = [4, 5, 7, 2]`
3. Take the next element `2`. Insert it into the correct position:
   `arr = [2, 4, 5, 7]`

### Time Complexity:
- **Best case:** **O(n)** (if the list is already sorted)
- **Average case:** **O(n^2)** (for a randomly ordered list)
- **Worst case:** **O(n^2)** (if the list is in reverse order)

### Space Complexity:
- Auxiliary Space: **O(1)**

---

## 4. Merge Sort
Merge Sort is a **divide-and-conquer** sorting algorithm. It is efficient and stable. In this algorithm, the array is divided into two halves repeatedly until it can no longer be divided. Then, each subarray is sorted individually using the merge sort algorithm. Finally, all sorted subarrays are merged back together in sorted order.

### Time Complexity:
1. **Best Case:**
   - **O(n log n)**
   - When the array is already sorted or nearly sorted.

2. **Average Case:**
   - **O(n log n)**
   - When the array is randomly ordered.

3. **Worst Case:**
   - **O(n log n)**
   - When the array is sorted in reverse order.

### Auxiliary Space:
- **O(n)**: Additional space is required for the temporary array used during merging.

### How Merge Sort Works:
1. **Divide**: Split the array into two halves recursively.
2. **Conquer**: Sort each half using merge sort.
3. **Combine**: Merge the two sorted halves back into a single sorted array.

### Example:
#### Given Array:
`[38, 27, 43, 3, 9, 82, 10]`

#### Steps:
1. **Divide**:
   - Split into two halves:
     - Left: `[38, 27, 43, 3]`
     - Right: `[9, 82, 10]`

2. **Recursive Division**:
   - `[38, 27, 43, 3]` → `[38, 27]` and `[43, 3]`
   - `[9, 82, 10]` → `[9, 82]` and `[10]`
   - Continue dividing until single-element arrays:
     - `[38], [27], [43], [3], [9], [82], [10]`

3. **Merge Step**:
   - Merge `[38]` and `[27]` → `[27, 38]`
   - Merge `[43]` and `[3]` → `[3, 43]`
   - Merge `[9]` and `[82]` → `[9, 82]`
   - Merge `[27, 38]` and `[3, 43]` → `[3, 27, 38, 43]`
   - Merge `[9, 82]` and `[10]` → `[9, 10, 82]`
   - Merge `[3, 27, 38, 43]` and `[9, 10, 82]` → `[3, 9, 10, 27, 38, 43, 82]`

#### Final Sorted Array:
`[3, 9, 10, 27, 38, 43, 82]`

### Python Implementation:
```python
# Merge Function
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [arr[l + i] for i in range(n1)]
    R = [arr[m + 1 + i] for i in range(n2)]
    i = j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# Merge Sort Function
def merge_sort(arr, l, r):
    if l < r:
        m = (l + r) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)

# Example Usage
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
```

### Output:
```
Original array: [38, 27, 43, 3, 9, 82, 10]
Sorted array: [3, 9, 10, 27, 38, 43, 82]
```

---

## 5. Quick Sort
Quick Sort is a **divide-and-conquer** sorting algorithm. It works by choosing a random, first, or last element as the **pivot**. All elements smaller than the pivot are moved to its left, and all elements larger are moved to its right. This process is repeated recursively until only one element remains in each partition.

### How It Works:
1. **Choose Pivot**: Select a pivot element (random, first, or last element).
2. **Partition**: Rearrange elements such that:
   - Left of pivot: Elements smaller than pivot.
   - Right of pivot: Elements larger than pivot.
3. **Recursion**: Apply the same process to the left and right subarrays.
4. **Base Case**: Stop when a subarray has only one element.

### Time Complexity:
1. **Best Case**: Ω(n log n)
   - Occurs when the pivot element divides the array into two equal halves.
2. **Average Case**: Θ(n log n)
   - On average, the pivot divides the array into two parts (not necessarily equal).
3. **Worst Case**: O(n²)
   - Occurs when the smallest or largest element is always chosen as the pivot (e.g., already sorted arrays).

### Auxiliary Space:
- **O(n)**: Due to the recursive call stack.

### Example:
#### Input Array:
`[8, 3, 7, 6, 2]`

#### Steps:
1. **First Partition**:
   - Choose Pivot: `2`
   - Partition:
     - Left: `[ ]` (no elements smaller than `2`).
     - Pivot: `2`.
     - Right: `[8, 3, 7, 6]` (all elements larger than `2`).

Result: `[2, 3, 7, 6, 8]`

2. **Recursively Sort Right Subarray (`[3, 7, 6, 8]`)**:
   - Choose Pivot: `8`
   - Partition:
     - Left: `[3, 7, 6]`.
     - Pivot: `8`.
     - Right: `[ ]` (no elements larger than `8`).

Result: `[3, 7, 6, 8]`

3. **Recursively Sort Left Subarray (`[3, 7, 6]`)**:
   - Choose Pivot: `6`
   - Partition:
     - Left: `[3]`.
     - Pivot: `6`.
     - Right: `[7]`.

Result: `[3, 6, 7]`

#### Final Sorted Array:
`[2, 3, 6, 7, 8]`

### Python Implementation:
```python
# Quick Sort Function
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]  # Choose the last element as the pivot
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

# Example Usage
arr = [8, 3, 7, 6, 2]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
```

### Output:
```
Original array: [8, 3, 7, 6, 2]
Sorted array: [2, 3, 6, 7, 8]
