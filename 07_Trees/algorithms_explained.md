# 🧠 Tree Algorithms Explained (For Beginners!)

> **No jargon. Just plain English explanations.**

---

## Table of Contents
1. [The "Tree" Mental Model](#1-the-tree-mental-model)
2. [DFS vs BFS Traversal](#2-dfs-vs-bfs-traversal)
3. [Binary Search Tree (BST) Logic](#3-binary-search-tree-bst-logic)
4. [Recursive Solving Pattern](#4-recursive-solving-pattern)

---

## 1. The "Tree" Mental Model

### 📖 What is it?
A hierarchical structure. It has a **Root** at the top, and branches down to **Leaves**. No cycles allowed (you can't go in a circle).

### 🤔 The Real World Analogy
*   **File System:** Folders inside folders.
*   **HTML DOM:** `<body>` contains `<div>`, which contains `<p>`.
*   **Company Org Chart:** CEO -> VP -> Manager -> Intern.

### 💡 The Visual

```
       [1]        <-- Root
      /   \
    [2]   [3]     <-- Children of 1
   /   \     \
 [4]   [5]   [6]  <-- Leaves (No children)
```

### 💻 Python Node Definition

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

---

## 2. DFS vs BFS Traversal

### 📖 What is it?
How we visit every node in the tree.

### 1. DFS (Depth First Search) - "The Diver"
Goes as deep as possible down one path before backing up.
*   **Preorder:** Root -> Left -> Right
*   **Inorder:** Left -> Root -> Right (Sorted order for BST!)
*   **Postorder:** Left -> Right -> Root (Bottom-up)

```python
def dfs(root):
    if not root: return
    
    print(root.val) # Preorder
    dfs(root.left)
    dfs(root.right)
```

### 2. BFS (Breadth First Search) - "The Scanner"
Visits level by level. Uses a **Queue**.
See [Queue Algorithms Explained](../05_Queues/algorithms_explained.md) for details.

---

## 3. Binary Search Tree (BST) Logic

### 📖 What is it?
A tree with a special rule:
*   Everything in the **Left** subtree is **smaller**.
*   Everything in the **Right** subtree is **larger**.

### 🤔 The Problem It Solves
Searching in **O(log n)** time (like Binary Search in an array).

Example: Find `7`
```
       [5]
      /   \
    [2]   [8]
         /   \
       [6]   [9]
         \
         [7]
```
1.  Start at 5. `7 > 5`? Go Right.
2.  At 8. `7 < 8`? Go Left.
3.  At 6. `7 > 6`? Go Right.
4.  Found 7!

### 💻 The Code (Validate BST)

```python
def isValidBST(root):
    def valid(node, left, right):
        if not node: return True
        if not (left < node.val < right): return False
        
        return (valid(node.left, left, node.val) and 
                valid(node.right, node.val, right))
    
    return valid(root, float("-inf"), float("inf"))
```

### 📺 Learn More
- [NeetCode - Validate BST](https://www.youtube.com/watch?v=s6ATEkipzow)

---

## 4. Recursive Solving Pattern

### 📖 What is it?
Solving a big tree problem by solving it for the small sub-trees.

### 💡 The Intuition (The "Leap of Faith")
To solve `maxDepth(root)`, assume `maxDepth(root.left)` and `maxDepth(root.right)` **already work**.

1.  **Base Case:** If root is None, depth is 0.
2.  **Recursive Step:** Ask children for their depth.
3.  **Combine:** My depth = `1 + max(left_depth, right_depth)`.

### 💻 The Code (Max Depth)

```python
def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
```

### 💻 The Code (Same Tree)

```python
def isSameTree(p, q):
    if not p and not q: return True  # Both empty = True
    if not p or not q: return False # One empty = False
    if p.val != q.val: return False # Values mismatch = False
    
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
```

### 📺 Learn More
- [NeetCode - Max Depth](https://www.youtube.com/watch?v=hTM3phVI6YQ)
- [NeetCode - Invert Tree](https://www.youtube.com/watch?v=OnSn2XEQ4MY)

---

## 🎯 Quick Decision Guide

| Problem Type | Pattern |
|-------------|---------|
| "Level order", "Shortest path" | **BFS (Queue)** |
| "Max depth", "Path sum", "Diameter" | **DFS (Recursion)** |
| "Sorted order", "Kth smallest" | **Inorder DFS** |
| "Search value", "Validate" | **BST Property** |
| "Subtree", "Same Tree", "Symmetric" | **Double Recursion** |

---
