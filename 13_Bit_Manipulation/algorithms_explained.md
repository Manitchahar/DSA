# 🧠 Bit Manipulation Explained (For Beginners!)

> **No jargon. Just plain English explanations.**

---

## Table of Contents
1. [The "Bit" Mental Model](#1-the-bit-mental-model)
2. [The Magical "XOR"](#2-the-magical-xor-single-number)
3. [Counting Bits (The "n & n-1" Trick)](#3-counting-bits-the-n--n-1-trick)
4. [Bit Masking / Shifting](#4-bit-masking--shifting)

---

## 1. The "Bit" Mental Model

### 📖 What is it?
Looking at numbers as a sequence of `0`s and `1`s.
`5` -> `101`
`4` -> `100`

### 💻 Python Basics
*   `&` (AND): Both must be 1.
*   `|` (OR): Either can be 1.
*   `^` (XOR): Different = 1.
*   `~` (NOT): Flip all bits.
*   `<<` (Left Shift): Multiply by 2.
*   `>>` (Right Shift): Divide by 2.

---

## 2. The Magical "XOR" (Single Number)

### 📖 What is it?
`^` (Caret). It returns 1 if bits are DIFFERENT.

### 💡 The Properties
1.  `n ^ n = 0` (Anything XOR itself cancels out)
2.  `n ^ 0 = n` (Anything XOR zero is itself)
3.  `a ^ b ^ c = c ^ a ^ b` (Order doesn't matter)

### 🤔 The Problem It Solves
"Every number appears twice except one. Find the single one."
`[4, 1, 2, 1, 2]`

Calc: `4 ^ 1 ^ 2 ^ 1 ^ 2`
Rearrange: `4 ^ (1 ^ 1) ^ (2 ^ 2)`
Simplify: `4 ^ 0 ^ 0`
Result: `4`

### 💻 The Code

```python
def singleNumber(nums):
    res = 0
    for n in nums:
        res = res ^ n
    return res
```

### 📺 Learn More
- [NeetCode - Single Number](https://www.youtube.com/watch?v=qMPX1AOa83k)

---

## 3. Counting Bits (The "n & n-1" Trick)

### 📖 What is it?
Counting how many `1`s are in a number.

### 💡 The Trick
`n & (n - 1)` **removes the last 1-bit** from `n`.
*   `n = 100` (4)
*   `n-1 = 011` (3)
*   `n & (n-1) = 000`

We can loop this until `n` becomes 0. The number of loops = number of 1s.

### 💻 The Code (Number of 1 Bits)

```python
def hammingWeight(n):
    count = 0
    while n:
        n = n & (n - 1)
        count += 1
    return count
```

### 💻 The Code (Counting Bits 0 to n)
Using DP: `dp[i] = dp[i >> 1] + (i & 1)`
(Number of 1s in `i` is same as `i/2` plus `1` if `i` is odd).

```python
def countBits(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp
```

### 📺 Learn More
- [NeetCode - Number of 1 Bits](https://www.youtube.com/watch?v=5Km3utixwZs)

---

## 4. Bit Masking / Shifting

### 📖 What is it?
Creating a specific pattern of 0s and 1s to inspect or modify a number.

### 💡 The Operations
*   **Get ith bit:** `(n >> i) & 1`
*   **Set ith bit:** `n | (1 << i)`
*   **Missing Number:** XOR all indices vs XOR all values.

### 💻 The Code (Missing Number)
Input: `[3, 0, 1]`
Indices: `0, 1, 2` (missing 3 equivalent)
Total expected: `0 ^ 1 ^ 2 ^ 3`
Actual: `3 ^ 0 ^ 1`
Result: `(3^0^1^2^3) ^ (3^0^1) = 2`

```python
def missingNumber(nums):
    res = len(nums)
    for i in range(len(nums)):
        res += (i - nums[i]) # Sum diff also works!
        # Or: res = res ^ i ^ nums[i]
    return res
```

### 📺 Learn More
- [NeetCode - Reverse Bits](https://www.youtube.com/watch?v=UcoN6UjAI64)

---

## 🎯 Quick Decision Guide

| Problem Type | Pattern |
|-------------|---------|
| "Find duplicate/single" | **XOR** |
| "Count 1s" | **n & (n-1)** |
| "Swap/Reverse bits" | **Shift & Mask** |
| "Sum without +" | **XOR (Sum) & AND (Carry)** |

---
