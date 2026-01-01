# 🧠 Math & Geometry Explained (For Beginners!)

> **No jargon. Just plain English explanations.**

---

## Table of Contents
1. [Matrix Traversal (Spiral / Rotate)](#1-matrix-traversal-spiral--rotate)
2. [Big Number Math (Multiply Strings)](#2-big-number-math-multiply-strings)
3. [Fast Powers (Pow(x, n))](#3-fast-powers-powx-n)
4. [Cycle Detection (Happy Number)](#4-cycle-detection-happy-number)

---

## 1. Matrix Traversal (Spiral / Rotate)

### 📖 What is it?
Moving through a 2D grid in a fancy pattern instead of just left-to-right.

### 💡 The "Boundary" Technique (Spiral Matrix)
Define your 4 walls: `left`, `right`, `top`, `bottom`.
1.  Walk Left -> Right (along `top`). Move `top` down.
2.  Walk Top -> Bottom (along `right`). Move `right` left.
3.  Walk Right -> Left (along `bottom`). Move `bottom` up.
4.  Walk Bottom -> Top (along `left`). Move `left` right.
Repeat until walls crash into each other!

### 💻 The Code (Rotate Image)
Rotate 90 degrees clockwise *in-place*.
**Trick:**
1.  **Transpose:** Swap `(r, c)` with `(c, r)`. (Flips over diagonal).
2.  **Reflect:** Reverse every row.

```python
def rotate(matrix):
    n = len(matrix)
    # 1. Transpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    # 2. Reverse Rows
    for i in range(n):
        matrix[i].reverse()
```

### 📺 Learn More
- [NeetCode - Rotate Image](https://www.youtube.com/watch?v=fMSJSS7eO1w)

---

## 2. Big Number Math (Multiply Strings)

### 📖 What is it?
Computers have limits (64-bit integers). How do you calculate `99999999999 * 99999999999` without crashing? You simulate how humans do it on paper!

### 💡 The Visual
```
    123
  x  45
  -----
    615  (123 * 5)
   4920  (123 * 40)
  -----
   5535
```
**Key Insight:** `num1[i] * num2[j]` will be placed at indices `[i + j, i + j + 1]` in the result array.

---

## 3. Fast Powers (Pow(x, n))

### 📖 What is it?
Calculating `x^n` (2^100) efficiently.
Naive loop: O(n).
Fast way: O(log n).

### 💡 The Intuition
`2^10 = (2^5) * (2^5)`
`2^5 = 2 * (2^2) * (2^2)`
If we calculate half, we get the whole instantly.

### 💻 The Code

```python
def myPow(x, n):
    if n == 0: return 1
    if n < 0: return 1 / myPow(x, -n)
    
    half = myPow(x, n // 2)
    
    if n % 2 == 0:
        return half * half # Even
    else:
        return x * half * half # Odd
```

### 📺 Learn More
- [NeetCode - Pow(x, n)](https://www.youtube.com/watch?v=g9YQyYi4IQQ)

---

## 4. Cycle Detection (Happy Number)

### 📖 What is it?
"Sum of squares of digits". If you reach 1, you are happy. If you loop forever, you are sad.

### 💡 The Trick
This is a **Linked List Cycle** problem in disguise!
*   `Slow` calculates sum once.
*   `Fast` calculates sum twice.
If `Slow == Fast` (and it's not 1), we are stuck in a loop.

### 💻 The Code

```python
def isHappy(n):
    slow, fast = n, sumSq(n)
    
    while fast != 1 and slow != fast:
        slow = sumSq(slow)
        fast = sumSq(sumSq(fast))
        
    return fast == 1
```

### 📺 Learn More
- [NeetCode - Happy Number](https://www.youtube.com/watch?v=ljz85bxOYJ0)

---

## 🎯 Quick Decision Guide

| Problem Type | Pattern |
|-------------|---------|
| "Matrix Spiral / Rotate" | **Simulation** (Boundaries) |
| "Zero out Matrix" | **Use first row/col as flags** |
| "Power / Exponent" | **Recursion (Halving)** |
| "Infinite Loop check" | **Fast & Slow Pointers** |
| "Multiply Strings" | **Array Simulation** |

---
