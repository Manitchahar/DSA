# 📚 Recursion & Backtracking - Complete DSA Guide

> **Master the art of breaking problems into subproblems!**

---

## 🎯 What You'll Master

- Recursion fundamentals and patterns
- Backtracking for permutations, combinations, subsets
- N-Queens, Sudoku solver patterns
- 20+ curated LeetCode problems

---

## 🔥 Fundamentals

### Recursion Template

```python
def solve(problem):
    # 1. Base case
    if is_base_case(problem):
        return base_solution
    
    # 2. Reduce problem
    smaller_problem = reduce(problem)
    
    # 3. Recursive call
    sub_solution = solve(smaller_problem)
    
    # 4. Build solution
    return build_solution(sub_solution)
```

### Backtracking Template

```python
def backtrack(path, choices):
    # Base case: valid solution found
    if is_solution(path):
        result.append(path[:])  # Copy!
        return
    
    for choice in choices:
        if is_valid(choice):
            path.append(choice)      # Make choice
            backtrack(path, remaining_choices)
            path.pop()               # Undo choice
```

---

## 🎨 Essential Patterns

### 1️⃣ Subsets

```python
def subsets(nums):
    result = []
    
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(0, [])
    return result
```

### 2️⃣ Permutations

```python
def permutations(nums):
    result = []
    
    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path, used)
            path.pop()
            used[i] = False
    
    backtrack([], [False] * len(nums))
    return result
```

### 3️⃣ Combinations

```python
def combinations(n, k):
    result = []
    
    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(1, [])
    return result
```

### 4️⃣ Combination Sum

```python
def combination_sum(candidates, target):
    result = []
    
    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        if remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])  # i, not i+1: reuse allowed
            path.pop()
    
    backtrack(0, [], target)
    return result
```

### 5️⃣ N-Queens

```python
def solve_n_queens(n):
    result = []
    
    def is_valid(board, row, col):
        for r in range(row):
            if board[r] == col or \
               board[r] - r == col - row or \
               board[r] + r == col + row:
                return False
        return True
    
    def backtrack(row, board):
        if row == n:
            result.append(board[:])
            return
        
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(row + 1, board)
    
    backtrack(0, [-1] * n)
    return result
```

---

## 🧠 Pattern Recognition

| Problem Type | Pattern |
|--------------|---------|
| "All subsets" | Backtrack with include/exclude |
| "All permutations" | Backtrack with used array |
| "All combinations" | Backtrack with start index |
| "Partition" | Backtrack with validation |
| "Sudoku/N-Queens" | Backtrack with constraints |

---

## ⚠️ Common Mistakes

```python
# 1) Forgetting to copy the path
result.append(path)     # ❌ Same reference
result.append(path[:])  # ✅ Copy

# 2) Not undoing the choice
path.append(choice)
backtrack(...)
path.pop()  # ✅ Don't forget!
```

---

> 💡 **Pro Tip:** Draw the recursion tree for small inputs to understand the pattern!
