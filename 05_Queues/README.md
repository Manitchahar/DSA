# 📚 Queues - Complete DSA Guide (Python)

> **Master the FIFO (First-In-First-Out) data structure!**

---

## 🎯 What You'll Master

- Queue fundamentals and variations (Queue, Deque, Priority Queue)
- BFS pattern and level-order traversal
- Sliding window maximum using deque
- 15+ curated LeetCode problems

---

## 🔥 Fundamentals

### What is a Queue?

A **queue** is a linear data structure that follows **FIFO** (First-In-First-Out). Like a line at a store - first person in line is first to be served!

```
Queue Operations:
                    enqueue(4)               dequeue()
┌───┬───┬───┐                  ┌───┬───┬───┬───┐            ┌───┬───┬───┐
│ 1 │ 2 │ 3 │        →         │ 1 │ 2 │ 3 │ 4 │     →      │ 2 │ 3 │ 4 │
└───┴───┴───┘                  └───┴───┴───┴───┘            └───┴───┴───┘
front    back                 front        back           front    back
                                             ↑                ↑
                                          added           removed
```

### Types of Queues

| Type | Description | Use Case |
|------|-------------|----------|
| **Queue** | Basic FIFO | BFS, task scheduling |
| **Deque** | Double-ended, add/remove both ends | Sliding window max |
| **Priority Queue** | Elements ordered by priority | Dijkstra, top-K |
| **Circular Queue** | Fixed size, wraps around | Buffer management |

---

## 🐍 Python Implementation

### Using collections.deque (Recommended)

```python
from collections import deque

q = deque()

# Enqueue (add to back)
q.append(1)
q.append(2)
q.append(3)

# Dequeue (remove from front)
front = q.popleft()  # 1

# Peek front
front = q[0]

# Peek back
back = q[-1]

# Size and empty check
len(q)
len(q) == 0
```

### Deque (Double-Ended Queue)

```python
from collections import deque

dq = deque()

# Add to both ends
dq.append(1)       # Right: [1]
dq.appendleft(0)   # Left: [0, 1]

# Remove from both ends
dq.pop()           # Right: removes 1
dq.popleft()       # Left: removes 0
```

### Priority Queue / Heap

```python
import heapq

# Min-heap (smallest first)
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
smallest = heapq.heappop(heap)  # 1

# For max-heap, negate values
heapq.heappush(heap, -val)
largest = -heapq.heappop(heap)
```

---

## ⚡ Core Operations & Complexity

| Operation | deque | list (as queue) |
|-----------|-------|-----------------|
| append (enqueue back) | O(1) | O(1) |
| popleft (dequeue front) | O(1) | O(n) ❌ |
| appendleft | O(1) | O(n) ❌ |
| pop (from back) | O(1) | O(1) |
| Access ends | O(1) | O(1) |

> ⚠️ Never use `list.pop(0)` for queues - it's O(n)! Always use `deque`.

---

## 🎨 Essential Patterns

### 1️⃣ BFS (Breadth-First Search)

**The most important queue pattern!**

```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        print(node)  # Process node
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

### 2️⃣ Level-Order Tree Traversal

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
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result
```

### 3️⃣ Sliding Window Maximum (Monotonic Deque)

```python
def max_sliding_window(nums, k):
    from collections import deque
    
    dq = deque()  # Store indices, values decreasing
    result = []
    
    for i, num in enumerate(nums):
        # Remove elements outside window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove smaller elements (they'll never be max)
        while dq and nums[dq[-1]] < num:
            dq.pop()
        
        dq.append(i)
        
        # Add to result once window is full
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result
```

### 4️⃣ Shortest Path in Grid (BFS)

```python
def shortest_path(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(0, 0, 0)])  # (row, col, distance)
    visited = {(0, 0)}
    
    while queue:
        r, c, dist = queue.popleft()
        
        if r == rows - 1 and c == cols - 1:
            return dist
        
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))
    
    return -1
```

### 5️⃣ Rotting Oranges (Multi-source BFS)

```python
def oranges_rotting(grid):
    from collections import deque
    
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    
    # Find all rotten oranges and count fresh
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh += 1
    
    if fresh == 0:
        return 0
    
    minutes = 0
    while queue:
        r, c, time = queue.popleft()
        
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                minutes = time + 1
                queue.append((nr, nc, time + 1))
    
    return minutes if fresh == 0 else -1
```

---

## 🧠 Problem-Solving Framework

| Keyword | Pattern |
|---------|---------|
| "shortest path" | BFS |
| "level by level" | BFS with level tracking |
| "spreading/infection" | Multi-source BFS |
| "sliding window maximum" | Monotonic deque |
| "order of processing" | Queue simulation |
| "task scheduling" | Queue + priority |

---

## ⚠️ Common Pitfalls

### 1. Using list.pop(0)
```python
# ❌ O(n) - shifts all elements!
queue = [1, 2, 3]
queue.pop(0)

# ✅ O(1) - use deque
from collections import deque
queue = deque([1, 2, 3])
queue.popleft()
```

### 2. Not Marking Visited BEFORE Adding to Queue
```python
# ❌ Wrong - may add same node multiple times
if node not in visited:
    queue.append(node)
    visited.add(node)  # Too late!

# ✅ Correct - mark immediately
if node not in visited:
    visited.add(node)  # First!
    queue.append(node)
```

---

## 🏁 Mastery Checklist

- [ ] I use `deque` not `list` for queues
- [ ] I can implement BFS for graphs and trees
- [ ] I understand level-order traversal
- [ ] I can use monotonic deque for sliding window max
- [ ] I mark nodes as visited BEFORE enqueueing

---

## 📁 Directory Structure

```
05_Queues/
├── README.md
├── cheatsheet.md
├── algorithms_explained.md
├── leetcode_problems.md
└── solutions/
    ├── bfs/
    ├── level_order/
    └── sliding_window/
```

---

> 💡 **Pro Tip:** BFS = Queue, DFS = Stack (or recursion). If you need "shortest" or "level-by-level", use a queue!

Happy Coding! 🎯
