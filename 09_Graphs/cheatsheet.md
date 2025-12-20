# 🚀 Graphs Cheat Sheet - Python

---

## ⚡ Representations

```python
# Adjacency List (Most Common)
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)  # If undirected

# Grid as implicit graph
directions = [(0,1), (0,-1), (1,0), (-1,0)]
```

---

## 🎯 Pattern Templates

### BFS
```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append(nei)
```

### DFS
```python
def dfs(graph, node, visited):
    visited.add(node)
    for nei in graph[node]:
        if nei not in visited:
            dfs(graph, nei, visited)
```

### Islands (Grid)
```python
def num_islands(grid):
    def dfs(r, c):
        if not (0 <= r < len(grid) and 0 <= c < len(grid[0])) or grid[r][c] != '1':
            return
        grid[r][c] = '0'
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            dfs(r+dr, c+dc)
    
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1
    return count
```

### Topological Sort (Kahn's)
```python
def topo_sort(graph, n):
    indegree = [0] * n
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1
    
    queue = deque([i for i in range(n) if indegree[i] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)
    
    return result if len(result) == n else []
```

### Dijkstra
```python
def dijkstra(graph, start, n):
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]
    
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]: continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist
```

### Union-Find
```python
class UF:
    def __init__(self, n):
        self.p = list(range(n))
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.p[px] = py
            return True
        return False
```

---

## 🏷️ Pattern Recognition

| Keyword | Pattern |
|---------|---------|
| Shortest path (unweighted) | BFS |
| Shortest path (weighted) | Dijkstra |
| Connected components | DFS/Union-Find |
| Course schedule | Topological Sort |
| Islands/regions | Grid DFS/BFS |

---

> 📌 BFS = level-by-level, DFS = explore deep first
