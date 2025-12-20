# 🧠 Algorithms Explained (For Beginners!)

> **No jargon. Just plain English explanations.**

---

## Table of Contents
1. [Kadane's Algorithm](#1-kadanes-algorithm)
2. [Two Pointers](#2-two-pointers)
3. [Sliding Window](#3-sliding-window)
4. [Prefix Sum](#4-prefix-sum)
5. [Binary Search](#5-binary-search)
6. [Dutch National Flag](#6-dutch-national-flag)
7. [Moore's Voting](#7-moores-voting)
8. [Cyclic Sort](#8-cyclic-sort)

---

## 1. Kadane's Algorithm

### 📖 What is it?
A clever trick to find the **maximum sum of a contiguous subarray** in just one pass through the array.

### 🤔 The Problem It Solves
Given an array like `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`, find the contiguous subarray with the largest sum.

Answer: `[4, -1, 2, 1]` → sum = **6**

### 💡 The Intuition (Think Like This)
Imagine you're collecting coins along a path:
- At each step, you ask: **"Should I keep my current collection, or start fresh from here?"**
- If your collection (running sum) becomes negative, it's HURTING you. Start fresh!
- Always remember the best collection you've ever had.

![Kadane's Algorithm Logic](/c:/Users/manit/.gemini/antigravity/brain/880c0f9a-5cc6-46f2-a112-9a9b04561644/kadane_logic_1765921681594.png)

```
Array:  [-2,  1, -3,  4, -1,  2,  1, -5,  4]
         ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓
Current: -2   1  -2   4   3   5   6   1   5
         ↑       ↑       
      (start   (4 is better
       fresh)   than 4+(-2)=-2)
       
Best seen: 6 ✅
```

### 🔑 When To Use It
- **Keyword in problem:** "maximum subarray sum", "best/largest contiguous"
- **You need:** Find best consecutive group of elements
- **Array can have:** Negative numbers (otherwise just sum everything!)

### 💻 The Code (Memorize This!)
```python
def max_subarray(nums):
    current_sum = max_sum = nums[0]
    
    for num in nums[1:]:
        # Either extend current subarray OR start fresh from here
        current_sum = max(num, current_sum + num)
        # Remember the best we've seen
        max_sum = max(max_sum, current_sum)
    
    return max_sum
```

### 📺 Learn More
- [NeetCode - Maximum Subarray](https://www.youtube.com/watch?v=5WZl3MMT0Eg) (8 min)

---

## 2. Two Pointers

### 📖 What is it?
Using **two index variables** that move through the array (usually towards each other or in the same direction).

### 🤔 The Problem It Solves
Many problems! Most common: Find a pair that adds up to a target in a **sorted** array.

### 💡 The Intuition (Think Like This)

**Opposite Direction (Pincer Move):**

![Two Pointers Pincer](/c:/Users/manit/.gemini/antigravity/brain/880c0f9a-5cc6-46f2-a112-9a9b04561644/two_pointers_pincer_1765921698644.png)

```
Array: [1, 2, 3, 4, 6, 8, 9]
        ↑                 ↑
       Left             Right
       
Target = 10

1 + 9 = 10? Yes! Found it! ✅

If sum too small → move left pointer right (get bigger number)
If sum too big → move right pointer left (get smaller number)
```

**Same Direction (Fast & Slow):**
```
Remove duplicates from [1, 1, 2, 2, 3]

Slow stays at "valid" position
Fast scans ahead

[1, 1, 2, 2, 3]
 S  F           → 1 == 1, skip
 S     F        → 1 != 2, copy 2 to S+1, move S
[1, 2, 2, 2, 3]
    S     F     → 2 == 2, skip
    S        F  → 2 != 3, copy 3 to S+1
[1, 2, 3, 2, 3]
       S        → Done! First 3 elements are unique
```

### 🔑 When To Use It
- **Keywords:** "pair", "sorted array", "in-place", "two numbers that..."
- **Array is:** Usually sorted, or you need to sort first
- **You want:** O(1) space, avoid nested loops

### 💻 The Code Templates
```python
# Opposite direction (sorted array, find pair)
def find_pair(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1      # need bigger sum
        else:
            right -= 1     # need smaller sum
    return []

# Same direction (in-place modification)
def remove_duplicates(arr):
    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1
```

### 📺 Learn More
- [NeetCode - Two Sum II](https://www.youtube.com/watch?v=cQ1Oz4ckceM) (6 min)
- [NeetCode - 3Sum](https://www.youtube.com/watch?v=jzZsG8n2R9A) (12 min)

---

## 3. Sliding Window

### 📖 What is it?
A "window" (subarray) that slides across the array. You add elements from the right and remove from the left.

### 🤔 The Problem It Solves
Find the best/smallest/largest subarray that satisfies some condition.

### 💡 The Intuition (Think Like This)

Imagine looking through a **window frame** at an array:

![Sliding Window Visual](/c:/Users/manit/.gemini/antigravity/brain/880c0f9a-5cc6-46f2-a112-9a9b04561644/sliding_window_visual_1765921717104.png)

```
Find max sum of 3 consecutive elements:

Array: [2, 1, 5, 1, 3, 2]

Step 1: Window covers [2, 1, 5] → sum = 8
        [2, 1, 5, 1, 3, 2]
         -------
         
Step 2: Slide right! Remove 2, add 1
        [2, 1, 5, 1, 3, 2]
            -------
        sum = 8 - 2 + 1 = 7
        
Step 3: Slide right! Remove 1, add 3
        [2, 1, 5, 1, 3, 2]
               -------
        sum = 7 - 1 + 3 = 9 ← MAX! ✅
```

**Key insight:** Don't recalculate the whole window sum. Just subtract what leaves, add what enters!

### 🔑 When To Use It
- **Keywords:** "subarray", "substring", "consecutive", "contiguous", "window of size k"
- **You're looking for:** Something about consecutive elements
- **Two types:**
  - **Fixed window:** Size is given (e.g., "size k")
  - **Variable window:** Size changes based on condition

### 💻 The Code Templates
```python
# Fixed size window
def max_sum_k(arr, k):
    window_sum = sum(arr[:k])  # First window
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]  # Slide: add right, remove left
        max_sum = max(max_sum, window_sum)
    return max_sum

# Variable size window (find smallest subarray with sum >= target)
def min_subarray_sum(arr, target):
    left = 0
    current_sum = 0
    min_len = float('inf')
    
    for right in range(len(arr)):
        current_sum += arr[right]    # Expand window
        
        while current_sum >= target:  # Shrink while valid
            min_len = min(min_len, right - left + 1)
            current_sum -= arr[left]
            left += 1
    
    return min_len if min_len != float('inf') else 0
```

### 📺 Learn More
- [NeetCode - Sliding Window Explained](https://www.youtube.com/watch?v=GcW4mgmgSbw) (13 min)
- [NeetCode - Longest Substring Without Repeating](https://www.youtube.com/watch?v=wiGpQwVHdE0) (7 min)

---

## 4. Prefix Sum

### 📖 What is it?
Pre-calculate cumulative sums so you can find **any range sum in O(1)**.

### 🤔 The Problem It Solves
"What's the sum of elements from index 2 to 5?" — answer instantly!

### 💡 The Intuition (Think Like This)

Think of a **running total** like your bank balance:

![Prefix Sum Visual](/c:/Users/manit/.gemini/antigravity/brain/880c0f9a-5cc6-46f2-a112-9a9b04561644/prefix_sum_visual_1765921733436.png)

```
Array:      [3, 1, 4, 1, 5]
Prefix:  [0, 3, 4, 8, 9, 14]
             ↑  ↑  ↑  ↑  ↑
             |  |  |  |  sum of all
             |  |  |  sum of first 4
             |  |  sum of first 3
             |  sum of first 2
             sum of first 1

Range sum [1 to 3]? (elements: 1, 4, 1)
= prefix[4] - prefix[1]
= 9 - 3 = 6 ✅

It's like: "Balance after index 3" - "Balance before index 1"
```

### 🔑 When To Use It
- **Keywords:** "range sum", "subarray sum equals K", "sum between indices"
- **You need:** Multiple range sum queries
- **Trick:** Often combined with HashMap for "subarray sum = K" problems

### 💻 The Code Templates
```python
# Build prefix sum
def build_prefix(arr):
    prefix = [0]
    for num in arr:
        prefix.append(prefix[-1] + num)
    return prefix

# Query range [i, j] inclusive
def range_sum(prefix, i, j):
    return prefix[j + 1] - prefix[i]

# Count subarrays with sum = k (IMPORTANT PATTERN!)
def subarray_sum_k(arr, k):
    count = 0
    prefix_sum = 0
    seen = {0: 1}  # We've seen sum=0 once (empty prefix)
    
    for num in arr:
        prefix_sum += num
        # If (prefix_sum - k) exists, those subarrays sum to k!
        count += seen.get(prefix_sum - k, 0)
        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1
    
    return count
```

### 📺 Learn More
- [NeetCode - Subarray Sum Equals K](https://www.youtube.com/watch?v=fFVZt-6sgyo) (10 min)
- [NeetCode - Product of Array Except Self](https://www.youtube.com/watch?v=bNvIQI2wAjk) (9 min)

---

## 5. Binary Search

### 📖 What is it?
Cut the search space in **half** each step. Only works on **sorted** data!

### 🤔 The Problem It Solves
Find a target in a sorted array in O(log n) instead of O(n).

### 💡 The Intuition (Think Like This)

It's like the **"Guess the Number"** game:

![Binary Search Visual](/c:/Users/manit/.gemini/antigravity/brain/880c0f9a-5cc6-46f2-a112-9a9b04561644/binary_search_visual_1765921764357.png)

```
I'm thinking of a number 1-100. You have 7 guesses.

You: "50?"        Me: "Higher"
You: "75?"        Me: "Lower"
You: "62?"        Me: "Lower"
You: "56?"        Me: "Higher"
You: "59?"        Me: "Correct!" ✅

Each guess eliminates HALF the possibilities!
```

**Visually:**
```
Find 7 in [1, 3, 5, 7, 9, 11, 13]

[1, 3, 5, 7, 9, 11, 13]
          ↑
         mid = 7
         Found it! ✅

If target > mid: search right half
If target < mid: search left half
```

### 🔑 When To Use It
- **Keywords:** "sorted array", "find", "search", "O(log n)"
- **Array is:** SORTED (or has some monotonic property)
- **Variations:**
  - Find exact value
  - Find first occurrence
  - Find last occurrence
  - Search on answer (when checking is O(n) but answer space is huge)

### 💻 The Code Template
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1   # Search right half
        else:
            right = mid - 1  # Search left half
    
    return -1  # Not found
```

### 📺 Learn More
- [NeetCode - Binary Search](https://www.youtube.com/watch?v=s4DPM8ct1pI) (8 min)
- [NeetCode - Search in Rotated Array](https://www.youtube.com/watch?v=U8XENwh8Oy8) (11 min)

---

## 6. Dutch National Flag

### 📖 What is it?
Sort an array with only **3 distinct values** in one pass using 3 pointers.

### 🤔 The Problem It Solves
Sort an array of 0s, 1s, and 2s (like the Dutch flag: red, white, blue 🇳🇱).

### 💡 The Intuition (Think Like This)

Imagine sorting colored balls into 3 buckets:

![Dutch National Flag Buckets](/c:/Users/manit/.gemini/antigravity/brain/880c0f9a-5cc6-46f2-a112-9a9b04561644/dnf_buckets_visual_1765921784357.png)

```
Array: [2, 0, 2, 1, 1, 0]

Three pointers:
- low: where next 0 should go
- mid: current element being examined
- high: where next 2 should go

[2, 0, 2, 1, 1, 0]
 L              H
 M

mid=2 → swap with high, shrink high
[0, 0, 2, 1, 1, 2]
 L           H
 M

mid=0 → swap with low, advance both
[0, 0, 2, 1, 1, 2]
    L        H
    M

... continue until mid > high
```

### 🔑 When To Use It
- **Keywords:** "sort colors", "three values", "0s, 1s, 2s"
- **Array has:** Exactly 3 distinct values
- **You want:** O(n) time, O(1) space, single pass

### 💻 The Code Template
```python
def sort_colors(nums):
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
            # Don't increment mid! New element needs checking
```

### 📺 Learn More
- [NeetCode - Sort Colors](https://www.youtube.com/watch?v=4xbWSRZHqac) (8 min)

---

## 7. Moore's Voting Algorithm

### 📖 What is it?
Find the **majority element** (appears > n/2 times) in O(n) time, O(1) space.

### 🤔 The Problem It Solves
Find the element that appears more than half the time.

### 💡 The Intuition (Think Like This)

Imagine a **battle royale** where elements fight:
- Same elements team up (count +1)
- Different elements cancel out (count -1)
- When count = 0, pick a new candidate

The majority element has MORE than half, so it will **always survive!**

![Moore's Voting Battle](/c:/Users/manit/.gemini/antigravity/brain/880c0f9a-5cc6-46f2-a112-9a9b04561644/moore_voting_battle_1765921804276.png)

```
Array: [2, 2, 1, 1, 1, 2, 2]

candidate = 2, count = 1  (see 2)
candidate = 2, count = 2  (see 2, +1)
candidate = 2, count = 1  (see 1, -1)
candidate = 2, count = 0  (see 1, -1)
candidate = 1, count = 1  (count=0, new candidate!)
candidate = 1, count = 0  (see 2, -1)
candidate = 2, count = 1  (count=0, new candidate!)
candidate = 2, count = 2  (see 2, +1)

Winner: 2 ✅
```

### 🔑 When To Use It
- **Keywords:** "majority element", "more than n/2", "appears most"
- **Guarantee:** Element appears > n/2 times (otherwise verify!)

### 💻 The Code Template
```python
def majority_element(nums):
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    
    return candidate  # Verify if needed: nums.count(candidate) > len(nums)//2
```

### 📺 Learn More
- [NeetCode - Majority Element](https://www.youtube.com/watch?v=7pnhv842keE) (5 min)

---

## 8. Cyclic Sort

### 📖 What is it?
Sort an array where elements are in range **[1, n]** or **[0, n-1]** by putting each element at its "correct index".

### 🤔 The Problem It Solves
Find missing numbers, duplicates, or sort in O(n) when elements are in a known range.

### 💡 The Intuition (Think Like This)

Each number knows its home!

![Cyclic Sort Mapping](/c:/Users/manit/.gemini/antigravity/brain/880c0f9a-5cc6-46f2-a112-9a9b04561644/cyclic_sort_mapping_1765921822518.png)

- Number 1 should be at index 0
- Number 2 should be at index 1
- Number 5 should be at index 4
- ...

Just keep swapping until everyone is home:
```
Array: [3, 1, 5, 4, 2]
        ↑
        3 is here, but 3 should be at index 2!
        
Swap 3 with whatever is at index 2:
[5, 1, 3, 4, 2]
 ↑
 5 is here, but 5 should be at index 4!
 
Swap 5 with whatever is at index 4:
[2, 1, 3, 4, 5]
 ↑
 2 is here, but 2 should be at index 1!
 
Swap 2 with whatever is at index 1:
[1, 2, 3, 4, 5]
 ↑
 1 is at index 0. Perfect! Move to next.
 
All sorted! ✅
```

### 🔑 When To Use It
- **Keywords:** "numbers in range [1, n]", "find missing", "find duplicate"
- **Array has:** Elements in a predictable range
- **Classic problems:** Missing Number, Find Duplicate, First Missing Positive

### 💻 The Code Template
```python
def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        correct_idx = nums[i] - 1  # Where this number should be
        if nums[i] != nums[correct_idx]:
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        else:
            i += 1
    return nums

def find_missing(nums):
    cyclic_sort(nums)
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
    return len(nums) + 1
```

### 📺 Learn More
- [NeetCode - Missing Number](https://www.youtube.com/watch?v=WnPLSRLSANE) (6 min)
- [NeetCode - First Missing Positive](https://www.youtube.com/watch?v=8g78yfzMlao) (12 min)

---

## 9. Matrix (2D Array) Patterns

### 📖 What is it?
Dealing with grids (rows and columns). Common patterns include traversing in weird shapes (spiral, diagonal) or rotating the whole grid.

### 🤔 The Problem It Solves
"Print this matrix in spiral order" or "Rotate this image 90 degrees".

### 💡 The Intuition (Think Like This)
**Spiral Traversal:**
Imagine you are walking along the outside walls of a room.
1.  Walk **Right** to the end.
2.  Walk **Down** to the bottom.
3.  Walk **Left** to the start.
4.  Walk **Up**... but stop before you hit your previous path!
5.  Repeat with the inner box.

![Spiral Matrix Traversal](/c:/Users/manit/.gemini/antigravity/brain/880c0f9a-5cc6-46f2-a112-9a9b04561644/spiral_matrix_traversal.png)

> **Pro Tip:** Don't try to write one complex loop. Break it down: `top`, `bottom`, `left`, `right` boundaries. Move them inwards as you finish each row/col.

### 🔑 When To Use It
- **Keywords:** "Matrix", "Grid", "2D Array", "Spiral", "Rotate"
- **You need:** To visit cells in a specific non-standard order.

---

## 🎯 Quick Decision Guide

| "Sorted array" | Binary Search or Two Pointers |
| "Find pair" | Two Pointers (sorted) or HashMap (unsorted) |
| "Subarray sum/product" | Sliding Window (consecutive) or Prefix Sum |
| "Sort 0s, 1s, 2s" | Dutch National Flag |
| "Majority element" | Moore's Voting |
| "Numbers in range [1,n]" | Cyclic Sort |
| "Matrix / Grid" | Simulation (Spiral/Rotate) |

### 🌳 Decision Tree Visualization

```mermaid
graph TD
    A[Start: Analyzing the Problem] --> B{Array is Sorted?}
    B -- Yes --> C[Target Pair?]
    C -- Yes --> D[Two Pointers]
    C -- No --> E[Binary Search]
    
    B -- No --> F{Subarray / Substring?}
    F -- Yes --> G{Fixed Size?}
    G -- Yes --> H[Sliding Window (Fixed)]
    G -- No --> I{Consecutive Elements?}
    I -- Yes --> J[Sliding Window (Variable)]
    I -- No --> K[Prefix Sum]
    
    F -- No --> L{Special Values?}
    L -- Yes --> M{0s, 1s, 2s?}
    M -- Yes --> N[Dutch National Flag]
    M -- No --> O{Range 1 to N?}
    O -- Yes --> P[Cyclic Sort]
    O -- No --> Q{Majority Element?}
    Q -- Yes --> R[Moore's Voting]
    
    L -- No --> S{Optimize Space?}
    S -- Yes --> T[In-place Operations]
    S -- No --> U[HashMap / HashSet]
```

---

## 🐞 How to Debug Array Problems

Getting "Index Out of Range" or wrong answers? Check these common culprits:

### 1. The "Off-By-One" Trap
- **Problem:** Loop goes too far or not far enough.
- **Fix:**
    - `range(n)` goes from `0` to `n-1`.
    - `range(1, n)` goes from `1` to `n-1`.
    - If accessing `arr[i+1]`, stop loop at `n-1`.

### 2. The "Boundary" Check
- **Problem:** `left`, `right`, or sliding window pointers go negative or exceed `len(arr)`.
- **Fix:** ALways check bounds *before* accessing.
    ```python
    while right < len(arr) and arr[right] == target:  # Good order
    while arr[right] == target and right < len(arr):  # CRASH if right == len ❌
    ```

### 3. Edge Cases (The "Small" Tests)
Before submitting, manually run your code on:
- **Empty array:** `[]`
- **Single element:** `[5]`
- **Two elements:** `[1, 2]`
- **All same:** `[5, 5, 5]`
- **Sorted/Reversed:** `[1, 2, 3]` vs `[3, 2, 1]`

---

> 💡 **Pro tip:** Don't memorize code. Understand the **intuition**. If you can explain it to a 5-year-old, you've got it!
