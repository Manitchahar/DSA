# 🧠 Dynamic Programming Explained (For Beginners!)

> **No jargon. Just plain English explanations.**

---

## Table of Contents
1. [The "DP" Mental Model](#1-the-dp-mental-model)
2. [Memoization vs Tabulation](#2-memoization-vs-tabulation)
3. [Pattern 1: 1D DP (Fibonacci & Robber)](#3-pattern-1-1d-dp-fibonacci--robber)
4. [Pattern 2: 2D DP (Grid Paths)](#4-pattern-2-2d-dp-grid-paths)
5. [Pattern 3: LCS & Knapsack](#5-pattern-3-lcs--knapsack)

---

## 1. The "DP" Mental Model

### 📖 What is it?
DP is just **Recursion + Caching**. 
Instead of solving the same sub-problem 100 times, you solve it **once**, write the answer on a sticky note (Memoization), and reuse it later.

### 🤔 The Real World Analogy
*   **1+1+1+1+1+1+1+1 = ?**
    *   You count: "8".
*   **Write +1 at the end.**
    *   You instanty say "9". Why? You didn't recount. You used the "cached" value of 8.

---

## 2. Memoization vs Tabulation

### 🧠 Top-Down (Memoization)
"I need `dp[5]`. To get that I need `dp[4]`. Let me iterate down."
*   **Pros:** Easy to write (just add a cache to recursion). Natural.
*   **Cons:** Recursion limit stack overflow.

```python
memo = {}
def solve(n):
    if n in memo: return memo[n]
    if n <= 1: return n
    
    memo[n] = solve(n-1) + solve(n-2)
    return memo[n]
```

### 📊 Bottom-Up (Tabulation)
"I have `dp[0]` and `dp[1]`. I can build `dp[2]`, then `dp[3]`..."
*   **Pros:** Fast, saves memory (iterative).
*   **Cons:** Harder to think about initially.

```python
def solve(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

---

## 3. Pattern 1: 1D DP (Fibonacci & Robber)

### 📖 What is it?
The decision at `i` depends only on `i-1` or `i-2`.

### 💡 The Problem (House Robber)
"You can rob houses i, but if you rob i, you can't rob i-1."
**Recurrence:** `rob(i) = max(arr[i] + rob(i-2), rob(i-1))`

### 💻 The Code

```python
def rob(nums):
    rob1, rob2 = 0, 0
    
    for n in nums:
        # [rob1, rob2, n, ...]
        newRob = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = newRob
        
    return rob2
```

### 📺 Learn More
- [NeetCode - House Robber](https://www.youtube.com/watch?v=73r3KWiEvyk)

---

## 4. Pattern 2: 2D DP (Grid Paths)

### 📖 What is it?
Moving through a grid. The number of ways to get to `(r, c)` comes from `(r-1, c)` (Top) and `(r, c-1)` (Left).

### 💡 The Equation
`dp[r][c] = dp[r-1][c] + dp[r][c-1]`

### 💻 The Code (Unique Paths)

```python
def uniquePaths(m, n):
    row = [1] * n
    
    for i in range(m - 1):
        newRow = [1] * n
        for j in range(n - 2, -1, -1):
            newRow[j] = newRow[j+1] + row[j]
        row = newRow
        
    return row[0]
```

---

## 5. Pattern 3: LCS & Knapsack

### 📖 What is it?
Comparing two strings or picking items with weight/value.
This usually requires a 2D table where one axis is "Index in string A" and other is "Index in string B".

### 💡 The Equation (Longest Common Subsequence)
*   **Matches:** `if s1[i] == s2[j]: 1 + solve(i+1, j+1)`
*   **No Match:** `max(solve(i+1, j), solve(i, j+1))`

### 💻 The Code (LCS)

```python
def longestCommonSubsequence(text1, text2):
    dp = [[0 for j in range(len(text2) + 1)] 
             for i in range(len(text1) + 1)]
             
    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
                
    return dp[0][0]
```

### 📺 Learn More
- [NeetCode - LCS](https://www.youtube.com/watch?v=Ua0GhsJSlWM)

---

## 🎯 Quick Decision Guide

| Problem Type | Pattern |
|-------------|---------|
| "Nth way", "Fibonacci", "Climbing Stairs" | **1D DP** (Depend on prev 1 or 2) |
| "Grid paths", "Min path sum" | **2D DP** (Grid) |
| "String matches", "LCS", "Edit Dist" | **2D DP** (i, j indices) |
| "Subset Sum", "Knapsack", "Coin Change" | **Unbounded/0-1 Knapsack** |
| "Partition array" | **Subset Sum** |

---
