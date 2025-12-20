# 🚀 Dynamic Programming Cheat Sheet

---

## 🎯 Core Patterns

### Fibonacci / Climbing Stairs
```python
def climb(n):
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b
```

### House Robber
```python
def rob(nums):
    prev2, prev1 = 0, 0
    for n in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + n)
    return prev1
```

### Coin Change
```python
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for c in coins:
        for x in range(c, amount + 1):
            dp[x] = min(dp[x], dp[x-c] + 1)
    return dp[amount] if dp[amount] < float('inf') else -1
```

### LCS
```python
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
```

### LIS
```python
def lis(nums):
    from bisect import bisect_left
    sub = []
    for n in nums:
        i = bisect_left(sub, n)
        if i == len(sub): sub.append(n)
        else: sub[i] = n
    return len(sub)
```

---

## 🏷️ Pattern Recognition

| Keyword | Pattern |
|---------|---------|
| Min/max ways | DP |
| Number of ways | DP (count) |
| Is it possible | DP (boolean) |
| Subsequence | LCS/LIS |
| String edit | Edit Distance |
| Grid paths | 2D DP |
| Knapsack constraints | 0/1 or unbounded |

---

> 📌 Recursive → Memoize → Tabulate → Optimize Space
