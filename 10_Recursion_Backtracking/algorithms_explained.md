# 🧠 Recursion & Backtracking Explained (For Beginners!)

> **No jargon. Just plain English explanations.**

---

## Table of Contents
1. [The "Backtracking" Mental Model](#1-the-backtracking-mental-model)
2. [The "Take or Skip" Pattern](#2-the-take-or-skip-pattern-subsets)
3. [The "Slot Filling" Pattern](#3-the-slot-filling-pattern-permutations)
4. [Grid Backtracking](#4-grid-backtracking)

---

## 1. The "Backtracking" Mental Model

### 📖 What is it?
A way to find **all** possible solutions by exploring every path. If you hit a dead end, you "backtrack" (go back one step) and try a different path.

### 🤔 The Real World Analogy
*   **The Maze:** You walk until you hit a wall. You turn around (backtrack) to the last junction and go left instead of right.
*   **Decision Tree:** Ordering pizza.
    *   Crust? [Thin, Thick]
        *   Choose Thin -> Topping? [Pep, Veg]
            *   Choose Pep. (Done)
        *   Backtrack to Topping -> Choose Veg. (Done)
    *   Backtrack to Crust -> Choose Thick...

### 💡 The Visual
```
       []
     /    \
   [1]     []     (Decide: Include 1?)
   / \     / \
[1,2] [1] [2] []  (Decide: Include 2?)
```

---

## 2. The "Take or Skip" Pattern (Subsets)

### 📖 What is it?
For every item, you have two choices: **Take it** or **Leave it**.

### 🤔 The Problem It Solves
"Find all **Subsets**."
(Power Set of `[1, 2]` -> `[], [1], [2], [1, 2]`)

### 💻 The Code

```python
def subsets(nums):
    res = []
    subset = []
    
    def dfs(i):
        # Base Case: Processed all numbers
        if i >= len(nums):
            res.append(subset.copy())
            return
            
        # Decision 1: TAKE num[i]
        subset.append(nums[i])
        dfs(i + 1)
        
        # Backtrack (Undo decision 1)
        subset.pop()
        
        # Decision 2: SKIP num[i]
        dfs(i + 1)
        
    dfs(0)
    return res
```

### 📺 Learn More
- [NeetCode - Subsets](https://www.youtube.com/watch?v=REOH22Xwdkk)

---

## 3. The "Slot Filling" Pattern (Permutations)

### 📖 What is it?
You have `n` empty slots. For each slot, pick an available number.

### 🤔 The Problem It Solves
"Find all **Permutations** (Order matters)."
`[1, 2]` -> `[1, 2], [2, 1]`

### 💻 The Code

```python
def permute(nums):
    res = []
    
    # Using a frequency map or swapping in-place works. 
    # Here is the general "Used" set approach.
    
    def dfs(path, used):
        if len(path) == len(nums):
            res.append(path.copy())
            return
            
        for n in nums:
            if n not in used:
                used.add(n)
                path.append(n)
                dfs(path, used)
                # Backtrack
                path.pop()
                used.remove(n)
                
    dfs([], set())
    return res
```

### 📺 Learn More
- [NeetCode - Permutations](https://www.youtube.com/watch?v=s7AvT7cGdSo)

---

## 4. Grid Backtracking (Word Search)

### 📖 What is it?
Moving Up/Down/Left/Right in a grid to find a path, but marking cells as "visited" so you don't use them twice *in the current path*, then unmarking them when you leave.

### 💻 The Code

```python
def exist(board, word):
    rows, cols = len(board), len(board[0])
    path = set()
    
    def dfs(r, c, i):
        if i == len(word): return True
        
        if (r < 0 or c < 0 or r >= rows or c >= cols or 
            word[i] != board[r][c] or (r,c) in path):
            return False
            
        path.add((r, c))
        
        # Try all 4 directions
        res = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or
               dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
               
        path.remove((r, c)) # Backtrack!
        return res
        
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0): return True
            
    return False
```

### 📺 Learn More
- [NeetCode - Word Search](https://www.youtube.com/watch?v=pfiQ_PS1g8E)

---

## 🎯 Quick Decision Guide

| Problem Type | Pattern |
|-------------|---------|
| "Subsets", "Combinations" | **Take or Skip** (Index based) |
| "Permutations", "Orderings" | **Loop all, Skip used** |
| "Word Search", "Grid Path" | **Grid DFS** (Mark/Unmark) |
| "N-Queens" | **Constraint Backtracking** |

---
