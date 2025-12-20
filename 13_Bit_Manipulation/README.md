# 📚 Bit Manipulation - DSA Guide

> **Harness the power of binary!**

---

## ⚡ Essential Operations

```python
# AND, OR, XOR, NOT
a & b    # AND: both 1 → 1
a | b    # OR: either 1 → 1
a ^ b    # XOR: different → 1
~a       # NOT: flip all bits

# Shifts
a << n   # Left shift: multiply by 2^n
a >> n   # Right shift: divide by 2^n

# Common Tricks
n & 1           # Is odd?
n & (n-1)       # Remove lowest set bit
n & -n          # Isolate lowest set bit
n ^ n           # Always 0
a ^ b ^ b       # = a (XOR cancels)
```

---

## 🎨 Common Patterns

### Single Number (XOR all)
```python
def single_number(nums):
    result = 0
    for n in nums:
        result ^= n
    return result
```

### Count Set Bits
```python
def count_bits(n):
    count = 0
    while n:
        n &= (n - 1)  # Remove lowest set bit
        count += 1
    return count
```

### Power of Two
```python
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0
```

---

## 🎯 LeetCode Problems

| # | Problem | 📺 Video |
|---|---------|----------|
| 136 | [Single Number](https://leetcode.com/problems/single-number/) | [NeetCode](https://youtu.be/qMPX1AOa83k) |
| 191 | [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | [NeetCode](https://youtu.be/5Km3utixwZs) |
| 338 | [Counting Bits](https://leetcode.com/problems/counting-bits/) | [NeetCode](https://youtu.be/RyBM56RIWrM) |
| 190 | [Reverse Bits](https://leetcode.com/problems/reverse-bits/) | [NeetCode](https://youtu.be/UcoN6UjAI64) |
| 268 | [Missing Number](https://leetcode.com/problems/missing-number/) | [NeetCode](https://youtu.be/WnPLSRLSANE) |
| 371 | [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) | [NeetCode](https://youtu.be/gVUrDV4tZfY) |

---

> 💡 XOR is your friend: a ^ a = 0, a ^ 0 = a
