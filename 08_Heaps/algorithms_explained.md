# 🧠 Heap Algorithms Explained (For Beginners!)

> **No jargon. Just plain English explanations.**

---

## Table of Contents
1. [The "Heap" Mental Model](#1-the-heap-mental-model)
2. [Min-Heap vs Max-Heap](#2-min-heap-vs-max-heap)
3. [The "Top K" Pattern](#3-the-top-k-pattern)
4. [Two Heaps Pattern](#4-two-heaps-pattern)

---

## 1. The "Heap" Mental Model

### 📖 What is it?
A specific type of **Tree** that is really good at ONE thing: **Giving you the smallest (or largest) item instantly.**

### 🤔 The Real World Analogy
*   **A "To-Do" List by Priority:** You don't care about the 10th most important task. You just want the #1 most urgent one right now.
*   **Emergency Room Triage:** The patient in critical condition goes first, regardless of when they arrived.

### 💡 The Visual

**Min-Heap:** The root is the **smallest**. Every parent is smaller than its children.
```
       [2]        <-- Smallest!
      /   \
    [5]   [10]
   /   \
 [12]  [7]
```

**Array Representation:**
`[2, 5, 10, 12, 7]`

### 🔑 When To Use It
*   **Keywords:** "Top K", "Kth Largest", "Smallest", "Most Frequent", "Median".
*   **You need to:** Access the extreme (min or max) repeatedly.

### 💻 Python Basics
Python has a built-in min-heap: `heapq`.

```python
import heapq

nums = [5, 2, 10]
heapq.heapify(nums)      # O(n) -> [2, 5, 10]
small = heapq.heappop(nums) # Returns 2, O(log n)
heapq.heappush(nums, 1)  # Adds 1, O(log n)
```

---

## 2. Min-Heap vs Max-Heap

### 📖 The Catch
Python **ONLY** has a **Min-Heap**.
To get a **Max-Heap** (where root is biggest), we use a trick: **Multiply numbers by -1**.

### 💡 The Trick
Original: `[1, 5, 10]`
Negated:  `[-1, -5, -10]`
Heapify:  `[-10, -5, -1]` (Min-heap of negatives)
Pop:      `-10`
Result:   `-1 * -10 = 10` (The max!)

---

## 3. The "Top K" Pattern

### 📖 What is it?
"Find the K largest elements in a list."

### 🤔 The Intuition
You might think: "Sort the list and take the top K". That's `O(n log n)`.
**Better:** Use a Min-Heap of size K!
Keep only the "K winners" in the heap. If a new number is bigger than the smallest winner, kick the loser out and let the new guy in.

### 💡 The Visual (K=3)
Stream: `[5, 1, 10, 3, 20]`

1.  Heap: `[5]`
2.  Heap: `[1, 5]`
3.  Heap: `[1, 5, 10]` (Full!)
4.  See `3`: Is `3 > 1` (min)? Yes! Pop `1`, push `3`. Heap: `[3, 5, 10]`
5.  See `20`: Is `20 > 3` (min)? Yes! Pop `3`, push `20`. Heap: `[5, 10, 20]`

Result: Top 3 are `5, 10, 20`.

### 💻 The Code

```python
def findKthLargest(nums, k):
    # Min-heap of size K
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap) # Remove smallest
            
    return heap[0] # The Kth largest is the smallest in our "Top K" club
```

### 📺 Learn More
- [NeetCode - Kth Largest Element](https://www.youtube.com/watch?v=XEmy13g1Qxc)

---

## 4. Two Heaps Pattern

### 📖 What is it?
Using a **Min-Heap** AND a **Max-Heap** together.

### 🤔 The Problem It Solves
"Find the **Median** of a data stream."
(Median = the middle number).

### 💡 The Intuition
Split the data into two halves:
*   **Small Half (Max-Heap):** Stores the smaller numbers. Root is the *biggest* of the smalls (the middle-left).
*   **Large Half (Min-Heap):** Stores the larger numbers. Root is the *smallest* of the bigs (the middle-right).

The median is just looking at the roots!

```
Small (Max)    Large (Min)
   [3]            [4]
  /              /
[1]            [5]

Median = (3 + 4) / 2 = 3.5
```

### 💻 The Code (Find Median)

```python
class MedianFinder:
    def __init__(self):
        self.small = [] # Max heap (invert sign)
        self.large = [] # Min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        
        # Ensure order: max(small) <= min(large)
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        # Balance sizes
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0
```

### 📺 Learn More
- [NeetCode - Median from Stream](https://www.youtube.com/watch?v=itmhHWaHupI)

---

## 🎯 Quick Decision Guide

| Problem Type | Pattern |
|-------------|---------|
| "Kth Smallest/Largest" | **Heap (Size K)** |
| "Top K Frequent" | **Counter + Heap** |
| "Merge K Sorted" | **Heap** (Push head of each list) |
| "Median of Stream" | **Two Heaps** |
| "Schedule Tasks" | **Max Heap + Queue** |

---
