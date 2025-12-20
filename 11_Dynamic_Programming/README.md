# 📚 Dynamic Programming - Complete DSA Guide

> **Master the art of optimal substructure!**

---

## 🎯 What You'll Master

- DP fundamentals: overlapping subproblems, memoization
- Common patterns: Fibonacci, Knapsack, LCS, LIS
- Top-down vs Bottom-up approaches
- 30+ curated LeetCode problems

---

## 🔥 Fundamentals

### When is DP applicable?

1. **Optimal substructure:** Solution can be built from subproblems
2. **Overlapping subproblems:** Same subproblems solved multiple times

### Two Approaches

| Top-Down (Memoization) | Bottom-Up (Tabulation) |
|------------------------|------------------------|
| Recursive + cache | Iterative |
| Natural thinking | More efficient |
| May not use all states | Uses all states |

---

## 🎨 Essential Patterns

### 1️⃣ Fibonacci Pattern (1D DP)

```python
# Top-Down
def fib_memo(n, memo={}):
    if n <= 1: return n
    if n not in memo:
        memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]

# Bottom-Up
def fib_tab(n):
    if n <= 1: return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# Space Optimized
def fib_opt(n):
    if n <= 1: return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

### 2️⃣ Climbing Stairs

```python
def climb_stairs(n):
    if n <= 2: return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
```

### 3️⃣ House Robber

```python
def rob(nums):
    if not nums: return 0
    if len(nums) == 1: return nums[0]
    
    # dp[i] = max money robbing up to house i
    prev2, prev1 = 0, 0
    for num in nums:
        curr = max(prev1, prev2 + num)
        prev2, prev1 = prev1, curr
    return prev1
```

### 4️⃣ 0/1 Knapsack

```python
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], 
                              values[i-1] + dp[i-1][w - weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]
```

### 5️⃣ Coin Change

```python
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1
```

### 6️⃣ Longest Common Subsequence (LCS)

```python
def lcs(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]
```

### 7️⃣ Longest Increasing Subsequence (LIS)

```python
def lis(nums):
    if not nums: return 0
    dp = [1] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# O(n log n) with binary search
def lis_binary(nums):
    from bisect import bisect_left
    sub = []
    for num in nums:
        i = bisect_left(sub, num)
        if i == len(sub):
            sub.append(num)
        else:
            sub[i] = num
    return len(sub)
```

### 8️⃣ Edit Distance

```python
def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],    # delete
                                  dp[i][j-1],    # insert
                                  dp[i-1][j-1])  # replace
    
    return dp[m][n]
```

### 9️⃣ Grid Unique Paths

```python
def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]
```

---

## 🧠 Pattern Recognition

| Problem Type | DP State |
|--------------|----------|
| Fibonacci-like | dp[i] depends on dp[i-1], dp[i-2] |
| Grid paths | dp[i][j] = dp[i-1][j] + dp[i][j-1] |
| Knapsack | dp[i][w] = include or exclude item |
| String matching | dp[i][j] for substrings |
| LIS | dp[i] = longest ending at i |

---

## ⚠️ Common Mistakes

```python
# 1) Forgetting base cases
dp[0] = ...  # Always initialize!

# 2) Off-by-one in loops
for i in range(1, n+1):  # Often need +1

# 3) Wrong initialization
dp = [[0] * n] * m  # ❌ Same row reference
dp = [[0] * n for _ in range(m)]  # ✅
```

---

> 💡 **Pro Tip:** Start with recursive solution, then add memoization, then convert to tabulation if needed.
