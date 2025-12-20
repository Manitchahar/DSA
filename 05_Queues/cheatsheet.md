# 🚀 Queues Cheat Sheet - Python

> Quick reference for interviews and problem-solving

---

## ⚡ Queue Operations

```python
from collections import deque

# ═══════════════════════════════════════════════════════
# BASIC QUEUE (FIFO)
# ═══════════════════════════════════════════════════════
q = deque()

q.append(x)          # Enqueue (add to back) - O(1)
q.popleft()          # Dequeue (remove front) - O(1)
q[0]                 # Peek front - O(1)
q[-1]                # Peek back - O(1)
len(q)               # Size
len(q) == 0          # Is empty?

# ═══════════════════════════════════════════════════════
# DEQUE (Double-Ended)
# ═══════════════════════════════════════════════════════
dq = deque()

dq.append(x)         # Add right
dq.appendleft(x)     # Add left
dq.pop()             # Remove right
dq.popleft()         # Remove left

# ═══════════════════════════════════════════════════════
# PRIORITY QUEUE (Min-Heap)
# ═══════════════════════════════════════════════════════
import heapq

heap = []
heapq.heappush(heap, val)   # Push
heapq.heappop(heap)         # Pop smallest
heap[0]                      # Peek smallest

# Max-heap: negate values
heapq.heappush(heap, -val)
-heapq.heappop(heap)        # Get largest
```

---

## 🎯 Pattern Templates

### BFS Template
```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        # Process node here
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

### Level-Order Traversal
```python
def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    
    return result
```

### Shortest Path in Grid
```python
def shortest_path(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(0, 0, 0)])  # row, col, dist
    visited = {(0, 0)}
    
    while queue:
        r, c, dist = queue.popleft()
        if r == rows-1 and c == cols-1:
            return dist
        
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in visited and grid[nr][nc] == 0:
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))
    return -1
```

### Sliding Window Maximum (Monotonic Deque)
```python
def max_sliding_window(nums, k):
    dq = deque()  # Indices, values decreasing
    result = []
    
    for i, num in enumerate(nums):
        # Remove outside window
        while dq and dq[0] <= i - k:
            dq.popleft()
        # Remove smaller (never will be max)
        while dq and nums[dq[-1]] < num:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result
```

### Multi-Source BFS (Rotting Oranges)
```python
def multi_source_bfs(grid):
    queue = deque()
    # Add all sources
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == SOURCE:
                queue.append((r, c, 0))
    
    while queue:
        r, c, dist = queue.popleft()
        # Spread to neighbors...
```

---

## 📊 Complexity Reference

| Operation | deque | list |
|-----------|-------|------|
| append | O(1) | O(1) |
| popleft | O(1) | O(n) ❌ |
| appendleft | O(1) | O(n) ❌ |
| pop | O(1) | O(1) |
| Access [0] | O(1) | O(1) |

---

## 🏷️ Pattern Recognition

| Keyword | Pattern |
|---------|---------|
| "shortest path" (unweighted) | BFS |
| "minimum steps" | BFS |
| "level by level" | BFS + level size |
| "spreading/expanding" | Multi-source BFS |
| "sliding window max/min" | Monotonic deque |
| "process in order" | Simple queue |

---

## ⚠️ Gotchas

```python
# 1) NEVER use list.pop(0) - it's O(n)!
queue.pop(0)       # ❌ O(n)
queue.popleft()    # ✅ O(1)

# 2) Mark visited BEFORE adding to queue
visited.add(node)  # First!
queue.append(node) # Then add

# 3) For BFS shortest path, return when DEQUEUING, not when adding
# (or return dist when adding, but it's dist+1 for neighbors)
```

---

> 📌 **Remember:** BFS = Queue, DFS = Stack/Recursion
