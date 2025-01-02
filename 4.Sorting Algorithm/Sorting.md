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
- Auxiliary Space: **O(1)** (Insertion Sort requires only a constant amount of additional memory.)

