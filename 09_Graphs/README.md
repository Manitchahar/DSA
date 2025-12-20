# 📚 Graphs - Complete DSA Guide (Python)

> **Master connected data structures!**

---

## 🎯 What You'll Master

- Graph representations and terminology
- BFS and DFS traversals
- Essential algorithms: Dijkstra, Topological Sort, Union-Find
- 25+ curated LeetCode problems

---

## 🔥 Fundamentals

### What is a Graph?

A **graph** is a collection of **nodes (vertices)** connected by **edges**.

```
Undirected:        Directed:
  A --- B           A → B
  |     |           ↓   ↓
  C --- D           C → D
```

### Key Terms

| Term | Definition |
|------|------------|
| **Vertex/Node** | A point in the graph |
| **Edge** | Connection between vertices |
| **Directed** | Edges have direction (A→B) |
| **Undirected** | Edges go both ways |
| **Weighted** | Edges have costs |
| **Cycle** | Path that returns to start |
| **Connected** | All nodes reachable |

### Graph Representations

```python
# Adjacency List (Most Common)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

# Adjacency Matrix
#     A  B  C  D
# A [[0, 1, 1, 0],
# B  [1, 0, 0, 1],
# C  [1, 0, 0, 1],
# D  [0, 1, 1, 0]]

# Edge List
edges = [['A','B'], ['A','C'], ['B','D'], ['C','D']]
```

---

## 🎨 Essential Patterns

### 1️⃣ BFS (Shortest Path in Unweighted)

```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

### 2️⃣ DFS (Explore All Paths)

```python
def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Iterative
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                stack.append(neighbor)
```

### 3️⃣ Number of Islands (Grid DFS/BFS)

```python
def num_islands(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'  # Mark visited
        dfs(r+1, c); dfs(r-1, c); dfs(r, c+1); dfs(r, c-1)
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1
    return count
```

### 4️⃣ Topological Sort (DAG Ordering)

```python
def topological_sort(graph):
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    
    queue = deque([u for u in in_degree if in_degree[u] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result if len(result) == len(graph) else []  # Empty if cycle
```

### 5️⃣ Detect Cycle

```python
# Undirected - DFS with parent tracking
def has_cycle_undirected(graph, node, visited, parent):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            if has_cycle_undirected(graph, neighbor, visited, node):
                return True
        elif neighbor != parent:
            return True
    return False

# Directed - DFS with colors
def has_cycle_directed(graph):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {u: WHITE for u in graph}
    
    def dfs(node):
        color[node] = GRAY
        for neighbor in graph[node]:
            if color[neighbor] == GRAY:
                return True
            if color[neighbor] == WHITE and dfs(neighbor):
                return True
        color[node] = BLACK
        return False
    
    return any(color[u] == WHITE and dfs(u) for u in graph)
```

### 6️⃣ Dijkstra (Shortest Path Weighted)

```python
import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    heap = [(0, start)]
    
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            if dist[node] + weight < dist[neighbor]:
                dist[neighbor] = dist[node] + weight
                heapq.heappush(heap, (dist[neighbor], neighbor))
    
    return dist
```

### 7️⃣ Union-Find (Disjoint Sets)

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # Already connected
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True
```

---

## 🧠 Pattern Recognition

| Keyword | Pattern |
|---------|---------|
| "shortest path" (unweighted) | BFS |
| "shortest path" (weighted) | Dijkstra |
| "connected components" | DFS/BFS or Union-Find |
| "is there a path" | BFS/DFS |
| "course schedule" / "dependencies" | Topological Sort |
| "islands" / "regions" | DFS/BFS on grid |
| "all paths" | DFS backtracking |
| "minimum spanning tree" | Prim's / Kruskal's |

---

## 📁 Directory Structure

```
09_Graphs/
├── README.md
├── cheatsheet.md
├── algorithms_explained.md
├── leetcode_problems.md
└── solutions/
    ├── bfs_dfs/
    ├── topological/
    └── union_find/
```

---

> 💡 **Pro Tip:** BFS = shortest path (unweighted), DFS = explore all / detect cycles

Happy Coding! 🎯
