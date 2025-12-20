# 🧠 Queue Algorithms Explained (For Beginners!)

> **No jargon. Just plain English explanations.**

---

## Table of Contents
1. [The "Queue" Mental Model](#1-the-queue-mental-model)
2. [Breadth-First Search (BFS)](#2-breadth-first-search-bfs)
3. [Level-Order Traversal](#3-level-order-traversal)
4. [Shortest Path in Grids](#4-shortest-path-in-grids)

---

## 1. The "Queue" Mental Model

### 📖 What is it?
A FIFO (First-In, First-Out) data structure. The first one to join the line is the first one to get served.

### 🤔 The Real World Analogy
*   **A line at Starbucks:** You join at the back. The person at the front gets their coffee and leaves. The cashier doesn't randomly pick the last person (unless it's a frantic LIFO situation!).
*   **Printer Job Spool:** You send a document. It waits for the previous documents to finish printing.

### 💡 The Visual

```
       Front                      Back
       ------------------------------
Out <- [1]  [2]  [3]  [4]  [5]  <-- In
       ------------------------------
       
Deque 1 (PopLeft) -> Returns 1
In is 6 (Append)
       
       ------------------------------
Out <- [2]  [3]  [4]  [5]  [6]  <-- 
       ------------------------------
```

### 🔑 When To Use It
*   **Keywords:** "Shortest path", "Level by level", "Order of arrival", "FCFS (First Come First Serve)".
*   **You need to:** Process things in layers or FAIRLY.

### 💻 Python Basics
In Python, **DO NOT** use a `list` for queues (removing from index 0 is slow `O(n)`).
Use `collections.deque`!

```python
from collections import deque

q = deque()
q.append(1)    # Push to back
val = q.popleft() # Pop from front (O(1))
```

---

## 2. Breadth-First Search (BFS)

### 📖 What is it?
An algorithm to explore a tree or graph layer by layer. You visit all neighbors of a node before moving to the neighbors' neighbors.

### 🤔 The Problem It Solves
"What is the **shortest path** from A to B?" (in an unweighted graph).

### 💡 The Visual - The Ripple Effect
Throw a stone in a pond.
*   **Time 0:** The splash (Start Node)
*   **Time 1:** First ripple circle (Immediate neighbors)
*   **Time 2:** Second ripple circle (Neighbors of neighbors)
*   ...

Unlike DFS (which goes deep down one path like a maze runner hitting a dead end), BFS expands equally in all directions.

---

## 3. Level-Order Traversal

### 📖 What is it?
Just BFS applied to a generic Tree. Printing nodes row by row.

### 💡 The Pattern
1.  Put `root` in queue.
2.  While queue is not empty:
    3.  Count how many nodes are in the queue right now (`size`).
    4.  Loop `size` times (process the current level):
        5.  Pop node.
        6.  Add children to queue.

### 💻 The Code

```python
def levelOrder(root):
    if not root: return []
    
    res = []
    q = deque([root])
    
    while q:
        level = []
        for _ in range(len(q)):  # Lock the size!
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(level)
            
    return res
```

### 📺 Learn More
- [NeetCode - Level Order Traversal](https://www.youtube.com/watch?v=6ZnyEApgFYg)

---

## 4. Shortest Path in Grids

### 📖 What is it?
Finding the quickest way to get from `S` to `E` in a 2D matrix (like a maze), moving Up/Down/Left/Right.

### 💡 The Intuition
This is just Level-Order Traversal on a graph!
*   **Level 0:** Start cell.
*   **Level 1:** All cells 1 step away.
*   **Level 2:** All cells 2 steps away.
*   The first time you see the Target, that is the shortest path!

**Crucial:** You need a `visited` set to avoid cycles (going back and forth).

### 💻 The Code (Rotting Oranges)
Multi-source BFS! Start from *all* rotten oranges simultaneously.

```python
def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])
    q = deque()
    fresh = 0
    time = 0
    
    # 1. Initialize Queue with all rotten oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1
                
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    # 2. BFS
    while q and fresh > 0:
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in directions:
                row, col = r + dr, c + dc
                # Check bounds and if fresh
                if (0 <= row < rows and 0 <= col < cols and
                    grid[row][col] == 1):
                    grid[row][col] = 2
                    q.append((row, col))
                    fresh -= 1
        time += 1
        
    return time if fresh == 0 else -1
```

### 📺 Learn More
- [NeetCode - Rotting Oranges](https://www.youtube.com/watch?v=y704fEOx0s0)
- [NeetCode - Number of Islands](https://www.youtube.com/watch?v=pV2kpPD66nE)

---

## 🎯 Quick Decision Guide

| Problem Type | Pattern |
|-------------|---------|
| "Level order", "Horizontal" | **BFS** |
| "Shortest path" (Unweighted) | **BFS** |
| "Connected components" | **BFS or DFS** (BFS avoids stack overflow) |
| "Rotting Oranges", "Simultaneous spread" | **Multi-Source BFS** |
| "Sliding Window Max" | **Monotonic Queue** (Deque) |

---
