# 📚 Math & Geometry - DSA Guide

> **Common math patterns for coding interviews!**

---

## ⚡ Essential Math

```python
# GCD
import math
math.gcd(a, b)

# LCM
def lcm(a, b):
    return a * b // math.gcd(a, b)

# Check prime
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Sieve of Eratosthenes
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

# Modular arithmetic
(a + b) % m = ((a % m) + (b % m)) % m
(a * b) % m = ((a % m) * (b % m)) % m

# Power mod
pow(base, exp, mod)  # Built-in!
```

---

## 🎨 Matrix Patterns

### Rotate 90° Clockwise

```python
def rotate(matrix):
    n = len(matrix)
    # Transpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for row in matrix:
        row.reverse()
```

### Spiral Order

```python
def spiral_order(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)          # Top row
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop()) # Right column
        if matrix:
            result += matrix.pop()[::-1] # Bottom row reversed
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))# Left column reversed
    return result
```

---

## 🎯 LeetCode Problems

| # | Problem | 📺 Video |
|---|---------|----------|
| 48 | [Rotate Image](https://leetcode.com/problems/rotate-image/) | [NeetCode](https://youtu.be/fMSJSS7eO1w) |
| 54 | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | [NeetCode](https://youtu.be/BJnMZNwUk1M) |
| 73 | [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | [NeetCode](https://youtu.be/T41rL0L3Pnw) |
| 50 | [Pow(x, n)](https://leetcode.com/problems/powx-n/) | [NeetCode](https://youtu.be/g9YQyYi4IQQ) |
| 43 | [Multiply Strings](https://leetcode.com/problems/multiply-strings/) | [NeetCode](https://youtu.be/1vZswirL8Y8) |
| 66 | [Plus One](https://leetcode.com/problems/plus-one/) | Basic |
| 202 | [Happy Number](https://leetcode.com/problems/happy-number/) | [NeetCode](https://youtu.be/ljz85bxOYJ0) |

---

> 💡 For matrix problems: think about in-place operations using transpose + reverse!
