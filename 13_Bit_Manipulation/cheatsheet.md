# 🚀 Bit Manipulation Cheat Sheet

---

## ⚡ Operators

```python
a & b    # AND
a | b    # OR  
a ^ b    # XOR
~a       # NOT
a << n   # Left shift (×2ⁿ)
a >> n   # Right shift (÷2ⁿ)
```

---

## 🎯 Common Tricks

```python
n & 1           # Check odd
n & (n-1)       # Remove lowest set bit
n & -n          # Get lowest set bit
n ^ n           # Always 0
a ^ b ^ b       # = a
```

---

## Templates

### Single Number (Find unique)
```python
def single_number(nums):
    res = 0
    for n in nums:
        res ^= n
    return res
```

### Count Set Bits
```python
def count_bits(n):
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count
```

### Power of Two
```python
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0
```

---

> 📌 XOR: a ^ a = 0, a ^ 0 = a
