# 📚 Heaps / Priority Queues - Complete DSA Guide (Python)

> **Master the "get min/max efficiently" data structure!**

---

## 🎯 What You'll Master

- Heap fundamentals and heapify operations
- Python heapq module
- Essential patterns: Top-K, K-way Merge, Median
- 15+ curated LeetCode problems

---

## 🔥 Fundamentals

### What is a Heap?

A **heap** is a complete binary tree where each parent is smaller (min-heap) or larger (max-heap) than its children.

```
Min-Heap:        Max-Heap:
     1                9
    / \              / \
   3   2            7   8
  / \              / \
 7   4            3   5

Parent ≤ Children    Parent ≥ Children
```

### Key Properties

| Property | Description |
|----------|-------------|
| **Complete Tree** | All levels filled except last |
| **Heap Property** | Parent vs children relationship |
| **O(1) Get Min/Max** | Root is always min or max |
| **O(log n) Insert/Delete** | Reheapify after change |

---

## 🐍 Python Implementation (heapq)

```python
import heapq

# Create min-heap
heap = []

# Push - O(log n)
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

# Pop minimum - O(log n)
smallest = heapq.heappop(heap)  # 1

# Peek minimum - O(1)
smallest = heap[0]

# Push and pop in one operation
result = heapq.heappushpop(heap, 4)

# Replace root and return old root
result = heapq.heapreplace(heap, 0)

# Convert list to heap - O(n)
nums = [3, 1, 4, 1, 5]
heapq.heapify(nums)

# Top k smallest
k_smallest = heapq.nsmallest(k, nums)

# Top k largest
k_largest = heapq.nlargest(k, nums)
```

### Max-Heap (Negate Values)

```python
# Python only has min-heap, so negate for max-heap
max_heap = []
heapq.heappush(max_heap, -val)    # Push negated
largest = -heapq.heappop(max_heap) # Pop and negate back
```

### Heap with Custom Key

```python
# Use tuples: (priority, data)
heap = []
heapq.heappush(heap, (distance, node))
priority, node = heapq.heappop(heap)

# Or with counter for tie-breaking
counter = 0
heapq.heappush(heap, (priority, counter, data))
counter += 1
```

---

## 🎨 Essential Patterns

### 1️⃣ Top K Elements

```python
def top_k_frequent(nums, k):
    from collections import Counter
    freq = Counter(nums)
    return heapq.nlargest(k, freq.keys(), key=freq.get)

# Or with heap
def top_k_heap(nums, k):
    freq = Counter(nums)
    heap = []
    for num, count in freq.items():
        heapq.heappush(heap, (count, num))
        if len(heap) > k:
            heapq.heappop(heap)  # Remove smallest
    return [num for count, num in heap]
```

### 2️⃣ K Closest Points

```python
def k_closest(points, k):
    heap = []
    for x, y in points:
        dist = x*x + y*y
        heapq.heappush(heap, (-dist, x, y))  # Max-heap
        if len(heap) > k:
            heapq.heappop(heap)
    return [[x, y] for _, x, y in heap]
```

### 3️⃣ Merge K Sorted Lists/Arrays

```python
def merge_k_lists(lists):
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))
    
    dummy = ListNode(0)
    curr = dummy
    
    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next
```

### 4️⃣ Find Median from Data Stream

```python
class MedianFinder:
    def __init__(self):
        self.small = []  # Max-heap (negated)
        self.large = []  # Min-heap
    
    def addNum(self, num):
        heapq.heappush(self.small, -num)
        
        # Balance: small's max ≤ large's min
        if self.small and self.large and -self.small[0] > self.large[0]:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        
        # Size balance
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))
    
    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
```

### 5️⃣ Task Scheduler

```python
def least_interval(tasks, n):
    freq = Counter(tasks)
    max_heap = [-f for f in freq.values()]
    heapq.heapify(max_heap)
    
    time = 0
    queue = []  # (available_time, count)
    
    while max_heap or queue:
        time += 1
        if max_heap:
            count = heapq.heappop(max_heap) + 1
            if count < 0:
                queue.append((time + n, count))
        
        if queue and queue[0][0] == time:
            heapq.heappush(max_heap, queue.pop(0)[1])
    
    return time
```

---

## 🧠 Pattern Recognition

| Keyword | Pattern |
|---------|---------|
| "top k" / "k largest/smallest" | Heap of size k |
| "k closest" | Max-heap of size k |
| "merge k sorted" | Min-heap with k elements |
| "median in stream" | Two heaps (max + min) |
| "schedule tasks" | Max-heap + cooldown queue |

---

## ⚠️ Common Pitfalls

```python
# 1) Python has MIN-heap only
heapq.heappush(heap, -val)  # Negate for max-heap

# 2) Can't peek empty heap
if heap:
    smallest = heap[0]

# 3) heapify is O(n), not O(n log n)
heapq.heapify(nums)  # In-place, O(n)
```

---

## 📁 Directory Structure

```
08_Heaps/
├── README.md
├── cheatsheet.md
├── algorithms_explained.md
├── leetcode_problems.md
└── solutions/
    ├── top_k/
    └── two_heaps/
```

---

> 💡 **Pro Tip:** For "top k", use a heap of size k. Push everything, pop when size > k!

Happy Coding! 🎯
