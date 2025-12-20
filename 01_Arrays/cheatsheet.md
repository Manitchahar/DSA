# 🚀 Arrays Cheat Sheet - Python

> Quick reference for interviews and problem-solving

---

## ⚡ Python List Operations

```python
# ═══════════════════════════════════════════════════════
# CREATION
# ═══════════════════════════════════════════════════════
arr = []                        # Empty list
arr = [1, 2, 3]                 # Initialize with values
arr = [0] * n                   # n zeros
arr = [i for i in range(n)]    # List comprehension
arr = list(range(n))           # Same as above

# 2D Array
matrix = [[0] * cols for _ in range(rows)]  # ✅ Correct
matrix = [[0] * cols] * rows                 # ❌ Wrong! Same row reference

# ═══════════════════════════════════════════════════════
# ACCESS & MODIFY
# ═══════════════════════════════════════════════════════
arr[0]                  # First element
arr[-1]                 # Last element
arr[1:4]                # Slice [1, 4)
arr[::-1]               # Reverse copy
arr[::2]                # Every 2nd element

# ═══════════════════════════════════════════════════════
# ADDING ELEMENTS
# ═══════════════════════════════════════════════════════
arr.append(x)           # Add to end - O(1)*
arr.insert(i, x)        # Insert at index - O(n)
arr.extend([1,2,3])     # Add multiple - O(k)
arr += [1, 2, 3]        # Same as extend

# ═══════════════════════════════════════════════════════
# REMOVING ELEMENTS
# ═══════════════════════════════════════════════════════
arr.pop()               # Remove last - O(1)
arr.pop(i)              # Remove at index - O(n)
arr.remove(x)           # Remove first x - O(n)
del arr[i]              # Delete at index - O(n)
arr.clear()             # Remove all - O(n)

# ═══════════════════════════════════════════════════════
# SEARCHING
# ═══════════════════════════════════════════════════════
x in arr                # Check existence - O(n)
arr.index(x)            # Find index (raises error if not found)
arr.count(x)            # Count occurrences - O(n)

# ═══════════════════════════════════════════════════════
# SORTING
# ═══════════════════════════════════════════════════════
arr.sort()              # In-place ascending
arr.sort(reverse=True)  # In-place descending
sorted(arr)             # Returns new sorted list
arr.sort(key=lambda x: x[1])  # Sort by custom key

# ═══════════════════════════════════════════════════════
# OTHER OPERATIONS
# ═══════════════════════════════════════════════════════
len(arr)                # Length - O(1)
min(arr), max(arr)      # Min/Max - O(n)
sum(arr)                # Sum - O(n)
arr.reverse()           # Reverse in-place - O(n)
arr.copy()              # Shallow copy - O(n)
```

---

## 🧰 Must-Know Python Tools (for Array Problems)

```python
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from itertools import accumulate
import heapq
import math

# bisect
i = bisect_left(a, x)      # first index with a[i] >= x
j = bisect_right(a, x)     # first index with a[j] > x

# prefix sums via accumulate
pref = [0] + list(accumulate(nums))
range_sum = pref[r + 1] - pref[l]

# top-k
topk = heapq.nlargest(k, nums)

# clean sentinels
best = math.inf
worst = -math.inf
```

---

## 🎯 Pattern Templates

### Two Pointers - Opposite Direction
```python
def two_pointers_opposite(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        # Process arr[left] and arr[right]
        if condition:
            left += 1
        else:
            right -= 1
```

### Two Pointers - Same Direction (Fast/Slow)
```python
def two_pointers_same(arr):
    slow = 0
    for fast in range(len(arr)):
        if condition:
            arr[slow] = arr[fast]
            slow += 1
    return slow
```

### Sliding Window - Fixed Size
```python
def sliding_window_fixed(arr, k):
    window = sum(arr[:k])
    result = window
    for i in range(k, len(arr)):
        window += arr[i] - arr[i - k]
        result = max(result, window)
    return result
```

### Sliding Window - Variable Size
```python
def sliding_window_variable(arr, target):
    left = 0
    window = 0
    result = float('inf')
    for right in range(len(arr)):
        window += arr[right]
        while window >= target:
            result = min(result, right - left + 1)
            window -= arr[left]
            left += 1
    return result
```

### Prefix Sum
```python
def prefix_sum(arr):
    prefix = [0]
    for num in arr:
        prefix.append(prefix[-1] + num)
    # Range sum [i, j] = prefix[j+1] - prefix[i]
    return prefix
```

### Prefix Sum + HashMap (Count subarrays sum = k)
```python
def count_subarrays_sum_k(nums, k):
    seen = {0: 1}
    pref = 0
    ans = 0
    for x in nums:
        pref += x
        ans += seen.get(pref - k, 0)
        seen[pref] = seen.get(pref, 0) + 1
    return ans
```

### Binary Search
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### Binary Search Boundaries (first >= x, last <= x)
```python
def first_ge(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if a[mid] >= x:
            hi = mid
        else:
            lo = mid + 1
    return lo

def last_le(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if a[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo - 1
```

### Binary Search on Answer (monotonic predicate)
```python
def first_true(lo, hi, ok):
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if ok(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

### Kadane's Algorithm
```python
def max_subarray(arr):
    max_current = max_global = arr[0]
    for num in arr[1:]:
        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)
    return max_global
```

### Difference Array (Range Updates)
```python
def apply_range_updates(n, updates):
    """updates = [(l, r, delta)] inclusive l..r"""
    diff = [0] * (n + 1)
    for l, r, delta in updates:
        diff[l] += delta
        if r + 1 < n:
            diff[r + 1] -= delta

    out = [0] * n
    run = 0
    for i in range(n):
        run += diff[i]
        out[i] = run
    return out
```

### Monotonic Stack (Next Greater Element)
```python
def next_greater(nums):
    n = len(nums)
    ans = [-1] * n
    st = []  # indices, values decreasing
    for i, x in enumerate(nums):
        while st and nums[st[-1]] < x:
            ans[st.pop()] = x
        st.append(i)
    return ans
```

### Monotonic Deque (Sliding Window Maximum)
```python
from collections import deque

def max_sliding_window(nums, k):
    dq = deque()  # indices, values decreasing
    out = []
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out
```

---

## 🔢 Quick Math Formulas

| Formula | Use Case |
|---------|----------|
| `n * (n + 1) // 2` | Sum of 1 to n |
| `n * (n - 1) // 2` | Number of pairs |
| `(n + k - 1) // k` | Ceiling division |
| `n & (n - 1)` | Remove lowest set bit |
| `n & -n` | Isolate lowest set bit |

---

## 📊 Complexity Reference

| Algorithm | Time | Space |
|-----------|------|-------|
| Two Pointers | O(n) | O(1) |
| Sliding Window | O(n) | O(1) |
| Prefix Sum | O(n) | O(n) |
| Binary Search | O(log n) | O(1) |
| Kadane's | O(n) | O(1) |
| QuickSort | O(n log n)* | O(log n) |
| MergeSort | O(n log n) | O(n) |
| HeapSort | O(n log n) | O(1) |
| Counting Sort | O(n + k) | O(k) |

---

## 💡 Pro Tips

### 1. Edge Cases Checklist
- Empty array `[]`
- Single element `[x]`
- Two elements
- All duplicates
- Already sorted / reverse sorted
- Negative numbers
- Very large numbers

### 2. Common Tricks
```python
# Swap without temp
a, b = b, a

# Get last element safely
last = arr[-1] if arr else None

# Initialize array with index
arr = list(range(n))

# Flatten 2D to 1D index
index = row * cols + col

# 1D to 2D indices
row, col = index // cols, index % cols

# Rotate array right by k
arr = arr[-k:] + arr[:-k]

# Check if sorted
is_sorted = all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
```

### 3. Python-Specific
```python
# zip for parallel iteration
for a, b in zip(arr1, arr2):
    ...

# enumerate for index + value
for i, val in enumerate(arr):
    ...

# any/all for conditions
has_positive = any(x > 0 for x in arr)
all_positive = all(x > 0 for x in arr)

# collections.Counter for frequency
from collections import Counter
freq = Counter(arr)
```

---

## ⚠️ Gotchas (Python Lists)

```python
# 1) 2D array aliasing (VERY common bug)
grid = [[0] * m for _ in range(n)]  # ✅
grid = [[0] * m] * n                # ❌ rows share same object

# 2) Slicing copies (space/time)
b = a[:]        # O(n) copy

# 3) Shallow copy vs deep copy
import copy
deep = copy.deepcopy(grid)

# 4) Don't modify list while iterating forward
for i in range(len(a) - 1, -1, -1):
    if a[i] == 0:
        a.pop(i)
```

---

## 🏷️ Pattern Recognition

| Keyword | Pattern |
|---------|---------|
| "sorted array" | Binary Search, Two Pointers |
| "pair with sum" | Two Pointers, HashMap |
| "subarray" | Sliding Window, Prefix Sum |
| "contiguous" | Sliding Window, Kadane's |
| "in-place" | Two Pointers |
| "k elements" | Heap, Sliding Window |
| "range [1,n]" | Cyclic Sort |
| "maximum/minimum sum" | Kadane's, DP |
| "majority element" | Moore's Voting |

---

> 📌 **Print this and keep it handy during practice!**
