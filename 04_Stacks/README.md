# 📚 Stacks - Complete DSA Guide (Python)

> **Master the LIFO (Last-In-First-Out) data structure!**

---

## 🎯 What You'll Master

- Stack fundamentals and operations
- Implementation using Python lists and deque
- Essential patterns: Monotonic Stack, Expression Evaluation, Parentheses
- 20+ curated LeetCode problems
- Common pitfalls and interview tips

---

## 📖 Table of Contents

1. [Fundamentals](#-fundamentals)
2. [Python Implementation](#-python-implementation)
3. [Core Operations & Complexity](#-core-operations--complexity)
4. [Essential Patterns](#-essential-patterns)
5. [Common Pitfalls](#-common-pitfalls)
6. [Mastery Checklist](#-mastery-checklist)

---

## 🔥 Fundamentals

### What is a Stack?

A **stack** is a linear data structure that follows **LIFO** (Last-In-First-Out). Think of a stack of plates - you can only add/remove from the top!

```
Stack Operations:
                  push(4)
     ┌───┐                    ┌───┐
     │ 3 │ ← top              │ 4 │ ← new top
     ├───┤           →        ├───┤
     │ 2 │                    │ 3 │
     ├───┤                    ├───┤
     │ 1 │                    │ 2 │
     └───┘                    ├───┤
                              │ 1 │
                              └───┘
```

### Key Properties

| Property | Description |
|----------|-------------|
| **LIFO** | Last element pushed is first one popped |
| **Single Access Point** | Only top element accessible |
| **O(1) Operations** | Push, pop, and peek are constant time |

### When to Use Stacks?

✅ **Use when:**
- Need to reverse something
- Matching/balancing (parentheses, tags)
- Tracking "most recent" or "undo" operations
- DFS traversal (recursion uses a stack!)
- Expression evaluation
- Next Greater/Smaller Element problems

---

## 🐍 Python Implementation

### Using Python List (Recommended)

```python
# Create a stack
stack = []

# Push
stack.append(1)
stack.append(2)
stack.append(3)

# Peek (view top without removing)
top = stack[-1]  # 3

# Pop (remove and return top)
top = stack.pop()  # 3

# Check if empty
is_empty = len(stack) == 0

# Size
size = len(stack)
```

### Using collections.deque

```python
from collections import deque

stack = deque()
stack.append(1)      # Push
top = stack[-1]       # Peek
top = stack.pop()     # Pop
```

### Stack Class (For Practice)

```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Pop from empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Peek from empty stack")
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
```

---

## ⚡ Core Operations & Complexity

| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| push(item) | O(1)* | O(1) | *Amortized for list |
| pop() | O(1) | O(1) | |
| peek() | O(1) | O(1) | Access `[-1]` |
| is_empty() | O(1) | O(1) | Check `len() == 0` |
| size() | O(1) | O(1) | |

---

## 🎨 Essential Patterns

### 1️⃣ Valid Parentheses

**The most classic stack problem!**

```python
def is_valid(s: str) -> bool:
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in '({[':
            stack.append(char)
        else:
            # Closing bracket - must match
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    
    return len(stack) == 0
```

### 2️⃣ Monotonic Stack (Next Greater Element)

**Find the next greater element for each element.**

```python
def next_greater_element(nums):
    n = len(nums)
    result = [-1] * n
    stack = []  # Stores indices
    
    for i in range(n):
        # While current element is greater than stack top
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    
    return result

# Example:
# nums = [2, 1, 2, 4, 3]
# result = [4, 2, 4, -1, -1]
```

**Decreasing Stack (Next Smaller):**
```python
def next_smaller_element(nums):
    n = len(nums)
    result = [-1] * n
    stack = []
    
    for i in range(n):
        while stack and nums[i] < nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    
    return result
```

### 3️⃣ Daily Temperatures (Days Until Warmer)

```python
def daily_temperatures(temperatures):
    n = len(temperatures)
    result = [0] * n
    stack = []  # Indices of days
    
    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_day = stack.pop()
            result[prev_day] = i - prev_day
        stack.append(i)
    
    return result
```

### 4️⃣ Evaluate Reverse Polish Notation

```python
def eval_rpn(tokens):
    stack = []
    operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: int(a / b)  # Truncate toward zero
    }
    
    for token in tokens:
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            stack.append(operators[token](a, b))
        else:
            stack.append(int(token))
    
    return stack[0]
```

### 5️⃣ Basic Calculator

```python
def calculate(s: str) -> int:
    stack = []
    num = 0
    sign = 1
    result = 0
    
    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == '+':
            result += sign * num
            num = 0
            sign = 1
        elif char == '-':
            result += sign * num
            num = 0
            sign = -1
        elif char == '(':
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ')':
            result += sign * num
            num = 0
            result *= stack.pop()  # Sign before (
            result += stack.pop()  # Result before (
    
    return result + sign * num
```

### 6️⃣ Min Stack

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self):
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.min_stack[-1]
```

### 7️⃣ Largest Rectangle in Histogram

```python
def largest_rectangle_area(heights):
    stack = []  # Indices
    max_area = 0
    heights.append(0)  # Sentinel to pop remaining
    
    for i, h in enumerate(heights):
        while stack and h < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    return max_area
```

---

## 🧠 Problem-Solving Framework

### Pattern Recognition

| Keyword | Pattern |
|---------|---------|
| "valid parentheses/brackets" | Stack matching |
| "next greater/smaller element" | Monotonic stack |
| "evaluate expression" | Stack + operators |
| "undo operation" | Stack to store history |
| "decode/simplify path" | Stack for components |
| "largest rectangle" | Monotonic stack |
| "trapping rain water" | Monotonic stack or two pointers |

---

## ⚠️ Common Pitfalls

### 1. Popping from Empty Stack

```python
# ❌ Crashes
stack.pop()  # Error if empty!

# ✅ Safe
if stack:
    stack.pop()
```

### 2. Wrong Pop Order for Operators

```python
# For "a - b", order matters!
# ❌ Wrong
a = stack.pop()
b = stack.pop()
result = a - b  # Actually computes the reverse!

# ✅ Correct
b = stack.pop()  # Second operand
a = stack.pop()  # First operand
result = a - b
```

### 3. Index vs Value in Monotonic Stack

```python
# Usually store INDICES, not values
stack.append(i)  # ✅ Index
# Access value via nums[stack[-1]]
```

---

## 🧪 Required Drills

- [ ] Implement Stack class from scratch
- [ ] Valid Parentheses (with different bracket types)
- [ ] Evaluate Reverse Polish Notation
- [ ] Next Greater Element pattern
- [ ] Min Stack with O(1) getMin
- [ ] Daily Temperatures
- [ ] Simplify Path

---

## 🏁 Mastery Checklist

- [ ] I can implement a stack using list
- [ ] I recognize matching/balancing as stack problems
- [ ] I understand monotonic stack for next greater/smaller
- [ ] I can evaluate expressions with a stack
- [ ] I handle edge cases: empty stack, single element

---

## 📁 Directory Structure

```
04_Stacks/
├── README.md              # This file
├── cheatsheet.md          # Quick reference
├── algorithms_explained.md # Deep dives
├── leetcode_problems.md   # Curated problems
└── solutions/
    ├── parentheses/
    ├── monotonic_stack/
    ├── expression_eval/
    └── design/
```

---

## 🚀 Next Steps

1. Read the [Cheat Sheet](./cheatsheet.md)
2. Study [Algorithms Explained](./algorithms_explained.md)
3. Practice [LeetCode Problems](./leetcode_problems.md)

---

> 💡 **Pro Tip:** When you see "next greater" or "next smaller", think monotonic stack immediately!

Happy Coding! 🎯
