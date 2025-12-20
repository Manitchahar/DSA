# 🚀 Heaps Cheat Sheet - Python

> Quick reference for heap problems

---

## ⚡ heapq Operations

```python
import heapq

heap = []

heapq.heappush(heap, x)      # Push - O(log n)
heapq.heappop(heap)          # Pop min - O(log n)
heap[0]                       # Peek min - O(1)

heapq.heapify(nums)          # List to heap - O(n)
heapq.nlargest(k, nums)      # Top k largest
heapq.nsmallest(k, nums)     # Top k smallest

heapq.heappushpop(heap, x)   # Push then pop
heapq.heapreplace(heap, x)   # Pop then push
```

### Max-Heap (Negate)

```python
heapq.heappush(heap, -val)
largest = -heapq.heappop(heap)
```

---

## 🎯 Pattern Templates

### Top K Elements

```python
def top_k(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap
```

### K Closest

```python
def k_closest(points, k):
    heap = []
    for p in points:
        dist = p[0]**2 + p[1]**2
        heapq.heappush(heap, (-dist, p))
        if len(heap) > k:
            heapq.heappop(heap)
    return [p for _, p in heap]
```

### Two Heaps (Median)

```python
class MedianFinder:
    def __init__(self):
        self.small = []  # Max-heap (negated)
        self.large = []  # Min-heap
    
    def add(self, num):
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))
    
    def median(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
```

---

## 📊 Complexity

| Operation | Time |
|-----------|------|
| Push | O(log n) |
| Pop | O(log n) |
| Peek | O(1) |
| Heapify | O(n) |

---

## 🏷️ Pattern Recognition

| Keyword | Pattern |
|---------|---------|
| "top k" | Min-heap size k |
| "k closest" | Max-heap size k |
| "median stream" | Two heaps |
| "merge k sorted" | Min-heap |

---

> 📌 Python only has min-heap. Negate for max-heap!
