# 🧠 Graph Algorithms Explained (For Beginners!)

> **No jargon. Just plain English explanations.**

---

## Table of Contents
1. [The "Graph" Mental Model](#1-the-graph-mental-model)
2. [DFS vs BFS (Graph Edition)](#2-dfs-vs-bfs-graph-edition)
3. [Topological Sort](#3-topological-sort-course-schedule)
4. [Union-Find (Disjoint Set)](#4-union-find-disjoint-set)

---

## 1. The "Graph" Mental Model

### 📖 What is it?
A collection of **Nodes** (Dots) and **Edges** (Lines connecting them).
*   **Directed:** One-way streets (A -> B).
*   **Undirected:** Two-way streets (A <-> B).

### 🤔 The Real World Analogy
*   **Social Network:** You are a node. Your friend is a node. The "friendship" is the edge.
*   **Google Maps:** Cities are nodes. Roads are edges.

### 💡 The Visual

```
    [A] ---> [B]
     |        |
     v        v
    [C] <--- [D]
```

### 💻 Adjacency List (How code sees it)
We use a HashMap (Dictionary) where Key = Node, Value = List of Neighbors.

```python
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": [],
    "D": ["C"]  # D points to C
}
```

---

## 2. DFS vs BFS (Graph Edition)

### 📖 The One Rule
**ALWAYS** use a `visited` set.
Graphs can have cycles (`A -> B -> A`). If you don't track where you've been, you'll loop forever!

### 💻 DFS (Deep Dive)
Good for: finding *any* path, counting islands.

```python
def dfs(node, visited):
    if node in visited: return
    visited.add(node)
    
    for neighbor in graph[node]:
        dfs(neighbor, visited)
```

### 💻 BFS (Wide Scan)
Good for: **Shortest Path** (unweighted).

```python
q = deque([start_node])
visited = {start_node}

while q:
    node = q.popleft()
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            q.append(neighbor)
```

---

## 3. Topological Sort (Course Schedule)

### 📖 What is it?
Putting nodes in a linear order where **dependencies come first**.
"I must take Calculus I before Calculus II".

### 🤔 The Problem It Solves
*   Build systems (Compile A before B).
*   Course scheduling.

### 💡 The Intuition
1.  Find a node with **0 dependencies** (No arrows pointing at it).
2.  "Do" that task. Remove it from the graph.
3.  Repeat.

### 💻 The Code (Kahn's Algorithm - BFS)

```python
def topologicalSort(numCourses, prerequisites):
    # 1. Build Graph & Indegree count
    graph = defaultdict(list)
    indegree = [0] * numCourses
    
    for dest, src in prerequisites:
        graph[src].append(dest)
        indegree[dest] += 1
        
    # 2. Start with 0-indegree nodes
    q = deque([i for i in range(numCourses) if indegree[i] == 0])
    order = []
    
    # 3. Process
    while q:
        course = q.popleft()
        order.append(course)
        
        for neighbor in graph[course]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
                
    return order if len(order) == numCourses else [] # Cycle check
```

### 📺 Learn More
- [NeetCode - Course Schedule](https://www.youtube.com/watch?v=EgI5nU9etnU)

---

## 4. Union-Find (Disjoint Set)

### 📖 What is it?
An efficient data structure to track "groups" or "components".
"Are A and B connected?"

### 🤔 The Problem It Solves
*   Counting connected components.
*   Detecting cycles in undirected graphs.
*   Minimum Spanning Tree (Kruskal's).

### 💡 The Visual
Every group has a "Leader" (Parent).
*   `[A, B, C]` are friends. `A` is the leader.
*   `[D, E]` are friends. `D` is the leader.
*   **Union(C, E):** Make `A` the parent of `D`. Now everyone follows `A`.

### 💻 The Code

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        
    def find(self, n):
        p = self.parent[n]
        # Path compression (Make tree flat!)
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
        
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False # Already connected
            
        # Union by Rank (Attach small to big)
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True
```

### 📺 Learn More
- [NeetCode - Union Find](https://www.youtube.com/watch?v=8f1XPm4WOUc)

---

## 🎯 Quick Decision Guide

| Problem Type | Pattern |
|-------------|---------|
| "Island", "Region", "Maze" | **DFS / BFS (Grid)** |
| "Shortest Path" | **BFS** |
| "Dependencies", "Order" | **Topological Sort** |
| "Connected?", "Redundant Edge" | **Union-Find** |
| "Shortest Path (Weighted)" | **Dijkstra** |

---
