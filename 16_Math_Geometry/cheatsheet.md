# 🚀 Math & Geometry Cheat Sheet

---

## ⚡ Python Math

```python
import math

math.gcd(a, b)          # GCD
math.lcm(a, b)          # LCM (Python 3.9+)
math.sqrt(n)            # Square root
math.ceil(x)            # Ceiling
math.floor(x)           # Floor
pow(base, exp, mod)     # Modular exponentiation
```

---

## 🎯 Matrix Templates

### Rotate 90° Clockwise
```python
def rotate(m):
    n = len(m)
    # Transpose
    for i in range(n):
        for j in range(i, n):
            m[i][j], m[j][i] = m[j][i], m[i][j]
    # Reverse rows
    for row in m:
        row.reverse()
```

### Spiral Order
```python
def spiral(m):
    res = []
    while m:
        res += m.pop(0)
        if m and m[0]:
            for row in m: res.append(row.pop())
        if m: res += m.pop()[::-1]
        if m and m[0]:
            for row in m[::-1]: res.append(row.pop(0))
    return res
```

---

## Common Math Tricks

```python
# Check prime
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

# GCD (Euclidean)
def gcd(a, b):
    while b: a, b = b, a % b
    return a
```

---

> 📌 For matrix: Transpose + Reverse = Rotate 90°
