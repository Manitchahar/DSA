# 📚 Arrays & Lists - Complete DSA Guide (Python)

> **Your journey to mastering Arrays starts here!**

---

## 🎯 What You'll Master

- Array fundamentals and internal workings
- Time & Space complexity for all operations
- Essential patterns and techniques
- 50+ curated LeetCode problems
- Pro tips, tricks, and common pitfalls

---

## ✅ How To Use This Folder (Do This In Order)

1. **Learn the concept** (read this README section-by-section)
2. **Memorize the templates** (see `cheatsheet.md`)
3. **Do the required drills** (below) until you can code them from memory
4. **Grind the curated LeetCode list** (see `leetcode_problems.md`) pattern-by-pattern
5. **Write 3-line notes per problem:** pattern, key insight, common bug

---

## 📖 Table of Contents

1. [Fundamentals](#-fundamentals)
2. [Python List Internals](#-python-list-internals)
3. [Core Operations & Complexity](#-core-operations--complexity)
4. [Essential Patterns](#-essential-patterns)
5. [Problem-Solving Framework](#-problem-solving-framework)
6. [Common Pitfalls](#-common-pitfalls)
7. [Required Drills (Non-LeetCode)](#-required-drills-non-leetcode)
8. [Mastery Checklist](#-mastery-checklist)

---

## 🔥 Fundamentals

### What is an Array?

An **array** is a contiguous block of memory storing elements of the same type, accessible via indices.

```
Index:    0     1     2     3     4
        ┌─────┬─────┬─────┬─────┬─────┐
Array:  │  5  │  2  │  8  │  1  │  9  │
        └─────┴─────┴─────┴─────┴─────┘
Memory: 1000  1004  1008  1012  1016  (assuming 4 bytes per int)
```

### Key Properties

| Property | Description |
|----------|-------------|
| **Fixed Size** | Traditional arrays have fixed size (Python lists are dynamic) |
| **Indexed Access** | O(1) random access via index |
| **Contiguous Memory** | Elements stored in consecutive memory locations |
| **Homogeneous** | All elements typically same type (Python allows mixed) |

---

## 🐍 Python List Internals

Python `list` is a **dynamic array** - it automatically resizes when needed.

### How Dynamic Resizing Works

```python
# When list is full and you append:
# 1. New array allocated (usually 1.125x or 2x size)
# 2. All elements copied to new array
# 3. Old array deallocated
# 4. New element added

# This is why append is "amortized O(1)"
```

### Memory Layout

```python
import sys

lst = []
for i in range(10):
    lst.append(i)
    print(f"Length: {len(lst)}, Size in bytes: {sys.getsizeof(lst)}")

# Output shows size grows in chunks, not per-element
```

### List vs Array (array module) vs NumPy

| Feature | list | array.array | numpy.array |
|---------|------|-------------|-------------|
| Mixed types | ✅ | ❌ | ❌ |
| Dynamic size | ✅ | ✅ | Fixed* |
| Memory efficient | ❌ | ✅ | ✅✅ |
| Speed | Slow | Medium | Fast |
| Use case | General | Typed data | Numerical |

### Python Toolkit You Should Use With Arrays

| Tool | When to use | Example |
|------|-------------|---------|
| `bisect` | Binary search + insertion point in sorted list | `bisect_left(a, x)` |
| `collections.Counter` | Frequency counting | `Counter(nums)` |
| `collections.defaultdict(int)` | Frequency with defaults | `d[x] += 1` |
| `itertools.accumulate` | Prefix sums without manual loop | `accumulate(nums)` |
| `heapq` | Top-k / k-largest | `heapq.nlargest(k, nums)` |
| `math.inf` | Clean min/max init | `best = math.inf` |

---

## ⚡ Core Operations & Complexity

### Time Complexity Cheat Sheet

| Operation | Average | Worst | Notes |
|-----------|---------|-------|-------|
| `arr[i]` Access | O(1) | O(1) | Index lookup |
| `arr[i] = x` Update | O(1) | O(1) | Direct write |
| `arr.append(x)` | O(1)* | O(n) | *Amortized |
| `arr.insert(i, x)` | O(n) | O(n) | Shifts elements |
| `arr.pop()` | O(1) | O(1) | Remove last |
| `arr.pop(i)` | O(n) | O(n) | Shifts elements |
| `arr.remove(x)` | O(n) | O(n) | Search + shift |
| `x in arr` | O(n) | O(n) | Linear search |
| `arr.index(x)` | O(n) | O(n) | Linear search |
| `len(arr)` | O(1) | O(1) | Stored value |
| `arr.sort()` | O(n log n) | O(n log n) | Timsort |
| `arr.reverse()` | O(n) | O(n) | In-place |
| `arr1 + arr2` | O(n + m) | O(n + m) | Creates new list |
| `arr * k` | O(n*k) | O(n*k) | Creates new list |
| `arr[a:b]` Slice | O(b-a) | O(b-a) | Creates copy |

### Space Complexity

| Operation | Space |
|-----------|-------|
| Most in-place ops | O(1) |
| Slice `arr[a:b]` | O(b-a) |
| `sorted(arr)` | O(n) |
| `arr.copy()` | O(n) |

---

## 🎨 Essential Patterns

### 1️⃣ Two Pointers

**When to use:** Sorted arrays, pair finding, palindromes, merging

```python
# Pattern: Opposite Direction
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

# Pattern: Same Direction (Fast & Slow)
def remove_duplicates(arr):
    if not arr:
        return 0
    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1
```

---

### 2️⃣ Sliding Window

**When to use:** Subarray problems, consecutive elements, fixed/variable window

```python
# Fixed Window
def max_sum_subarray(arr, k):
    if len(arr) < k:
        return None
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # Slide: add right, remove left
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Variable Window (Expand/Contract)
def min_subarray_len(target, arr):
    left = 0
    current_sum = 0
    min_len = float('inf')
    
    for right in range(len(arr)):
        current_sum += arr[right]  # Expand
        
        while current_sum >= target:  # Contract
            min_len = min(min_len, right - left + 1)
            current_sum -= arr[left]
            left += 1
    
    return min_len if min_len != float('inf') else 0
```

---

### 3️⃣ Prefix Sum

**When to use:** Range sum queries, subarray sum equals K

```python
# Build prefix sum
def build_prefix_sum(arr):
    prefix = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]
    return prefix

# Query range sum [i, j] inclusive
def range_sum(prefix, i, j):
    return prefix[j + 1] - prefix[i]

# Subarray sum equals K
def subarray_sum(arr, k):
    count = 0
    prefix_sum = 0
    sum_count = {0: 1}  # Handle subarrays starting from index 0
    
    for num in arr:
        prefix_sum += num
        
        # If (prefix_sum - k) exists, we found subarrays with sum k
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]
        
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
    
    return count
```

---

### 4️⃣ Binary Search

**When to use:** Sorted arrays, search space problems, finding boundaries

```python
# Standard Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Find Left Boundary (First occurrence)
def find_left_boundary(arr, target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left

# Find Right Boundary (Last occurrence)
def find_right_boundary(arr, target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    
    return left - 1
```

---

### 4️⃣.1 Binary Search “Answer Space” (Search on Result)

**When to use:** “minimize/maximize something” with a monotonic predicate (e.g., minimum capacity, minimum speed)

```python
def first_true(lo, hi, ok):
    """Return smallest x in [lo, hi] such that ok(x) is True."""
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if ok(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

---

### 5️⃣ Dutch National Flag (3-Way Partition)

**When to use:** Sort array with 3 distinct values, partition around pivot

```python
def sort_colors(nums):
    """Sort 0s, 1s, and 2s in-place"""
    low, mid, high = 0, 0, len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    
    return nums
```

---

### 6️⃣ Kadane's Algorithm

**When to use:** Maximum subarray sum

```python
def max_subarray(arr):
    max_ending_here = max_so_far = arr[0]
    
    for num in arr[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

# Variant: Track indices
def max_subarray_with_indices(arr):
    max_ending_here = max_so_far = arr[0]
    start = end = temp_start = 0
    
    for i in range(1, len(arr)):
        if arr[i] > max_ending_here + arr[i]:
            max_ending_here = arr[i]
            temp_start = i
        else:
            max_ending_here += arr[i]
        
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = temp_start
            end = i
    
    return max_so_far, start, end
```

---

### 7️⃣ Moore's Voting Algorithm

**When to use:** Find majority element (appears > n/2 times)

```python
def majority_element(arr):
    candidate = None
    count = 0
    
    # Phase 1: Find candidate
    for num in arr:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    
    # Phase 2: Verify (optional if guaranteed to exist)
    if arr.count(candidate) > len(arr) // 2:
        return candidate
    return None
```

---

### 8️⃣ Cyclic Sort

**When to use:** Arrays with elements in range [1, n] or [0, n-1]

```python
def cyclic_sort(arr):
    """Sort array with elements [1, n] in O(n) time, O(1) space"""
    i = 0
    while i < len(arr):
        correct_pos = arr[i] - 1
        if arr[i] != arr[correct_pos]:
            arr[i], arr[correct_pos] = arr[correct_pos], arr[i]
        else:
            i += 1
    return arr

def find_missing_number(arr):
    """Find missing number in [0, n]"""
    i = 0
    n = len(arr)
    
    while i < n:
        if arr[i] < n and arr[i] != arr[arr[i]]:
            arr[arr[i]], arr[i] = arr[i], arr[arr[i]]
        else:
            i += 1
    
    for i in range(n):
        if arr[i] != i:
            return i
    return n
```

---

### 9️⃣ Difference Array (Range Updates)

**When to use:** many range increment/decrement operations, then compute final array

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

---

## 🧠 Problem-Solving Framework

### Step 1: Understand the Problem
- What is the input/output?
- What are the constraints?
- Any edge cases? (empty array, single element, duplicates)

### Step 2: Identify the Pattern
Ask yourself:
- Is the array sorted? → **Binary Search**, **Two Pointers**
- Looking for pairs/triplets? → **Two Pointers**, **HashMap**
- Subarray problems? → **Sliding Window**, **Prefix Sum**
- Need to sort with constraints? → **Counting Sort**, **Cyclic Sort**
- Maximum/minimum subarray? → **Kadane's Algorithm**
- Elements in range [1,n]? → **Cyclic Sort**

### Step 3: Code & Optimize
- Start with brute force to understand
- Optimize using patterns
- Consider space-time tradeoffs

### Step 4: Test
- Empty array
- Single element
- All same elements
- Already sorted / reverse sorted
- Large numbers / negative numbers

---

## ⚠️ Common Pitfalls

### 1. Off-by-One Errors
```python
# ❌ Wrong
for i in range(len(arr)):
    print(arr[i + 1])  # IndexError at last element

# ✅ Correct
for i in range(len(arr) - 1):
    print(arr[i + 1])
```

### 2. Modifying While Iterating
```python
# ❌ Wrong - skips elements
for i, x in enumerate(arr):
    if x == 0:
        arr.pop(i)

# ✅ Correct - iterate backwards
for i in range(len(arr) - 1, -1, -1):
    if arr[i] == 0:
        arr.pop(i)

# ✅ Or use list comprehension
arr = [x for x in arr if x != 0]
```

### 3. Shallow vs Deep Copy
```python
# ❌ Shallow copy - nested lists still shared
arr2 = arr[:]
arr2 = arr.copy()
arr2 = list(arr)

# ✅ Deep copy
import copy
arr2 = copy.deepcopy(arr)
```

### 4. Integer Overflow in Binary Search
```python
# ❌ Potential overflow (not in Python, but habit for other languages)
mid = (left + right) // 2

# ✅ Safe calculation
mid = left + (right - left) // 2
```

### 5. Empty Array Checks
```python
# ❌ Crashes on empty array
max_val = arr[0]

# ✅ Always check
if not arr:
    return None  # or appropriate value
max_val = arr[0]
```

---

## 🧪 Required Drills (Non-LeetCode)

You should be able to code each of these in **≤ 10 minutes** without looking.

- [ ] Reverse array (in-place)
- [ ] Rotate array right by $k$ (O(1) extra space using reverse trick)
- [ ] Remove all occurrences of `x` in-place, return new length
- [ ] Remove duplicates from sorted array (in-place)
- [ ] Merge two sorted arrays (two pointers)
- [ ] Find pair sum in sorted array (two pointers)
- [ ] Maximum subarray sum (Kadane)
- [ ] Longest subarray with sum ≤/≥ target (sliding window, when valid)
- [ ] Count subarrays with sum = k (prefix sum + hashmap)
- [ ] Build prefix sums and answer range sum queries
- [ ] Find first/last occurrence of target in sorted array (binary search bounds)
- [ ] Matrix: transpose, rotate 90°, spiral traversal

---

## 🏁 Mastery Checklist

- [ ] I can explain why `append` is amortized O(1)
- [ ] I can choose the right pattern from keywords (“subarray”, “sorted”, “k”, “range updates”)
- [ ] I can write 2-pointer + sliding-window templates from memory
- [ ] I can implement `bisect_left` style boundaries without bugs
- [ ] I can do prefix-sum hashmap problems without re-deriving every time
- [ ] I can handle edge cases: empty, size-1, duplicates, negatives
- [ ] I can explain time/space for my solution quickly

---

## 📁 Directory Structure

```
01_Arrays/
├── README.md              # This file
├── cheatsheet.md          # Quick reference
├── leetcode_problems.md   # Curated problem list
└── solutions/             # Your practice code
    ├── two_pointers/
    ├── sliding_window/
    ├── prefix_sum/
    ├── binary_search/
    └── sorting/
```

---

## 🚀 Next Steps

1. **🆕 Confused by algorithms?** Read [Algorithms Explained (Beginner-Friendly!)](./algorithms_explained.md) first
2. **Read** the [Cheat Sheet](./cheatsheet.md) for quick reference
3. **Study** the [LeetCode Problems](./leetcode_problems.md) - now with video links!
4. **Practice** daily - start with Easy, move to Medium
5. **Track** your progress in the solutions folder

---

> 💡 **Pro Tip:** Don't just solve problems - understand WHY a pattern works. This transfers to new problems!

Happy Coding! 🎯
