# 🚀 Stacks Cheat Sheet - Python

> Quick reference for interviews and problem-solving

---

## ⚡ Stack Operations

```python
# ═══════════════════════════════════════════════════════
# USING LIST (Most Common)
# ═══════════════════════════════════════════════════════
stack = []

stack.append(x)      # Push - O(1)
stack.pop()          # Pop - O(1)
stack[-1]            # Peek - O(1)
len(stack) == 0      # Is empty?
len(stack)           # Size

# ═══════════════════════════════════════════════════════
# USING DEQUE
# ═══════════════════════════════════════════════════════
from collections import deque
stack = deque()

stack.append(x)      # Push
stack.pop()          # Pop
stack[-1]            # Peek
```

---

## 🎯 Pattern Templates

### Valid Parentheses
```python
def is_valid(s: str) -> bool:
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for c in s:
        if c in '({[':
            stack.append(c)
        else:
            if not stack or stack[-1] != pairs[c]:
                return False
            stack.pop()
    
    return len(stack) == 0
```

### Monotonic Stack - Next Greater Element
```python
def next_greater(nums):
    n = len(nums)
    result = [-1] * n
    stack = []  # Store indices!
    
    for i in range(n):
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    
    return result
```

### Monotonic Stack - Next Smaller Element
```python
def next_smaller(nums):
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

### Daily Temperatures
```python
def daily_temperatures(temps):
    n = len(temps)
    result = [0] * n
    stack = []
    
    for i in range(n):
        while stack and temps[i] > temps[stack[-1]]:
            prev = stack.pop()
            result[prev] = i - prev
        stack.append(i)
    
    return result
```

### Evaluate Reverse Polish Notation
```python
def eval_rpn(tokens):
    stack = []
    ops = {'+': lambda a,b: a+b, '-': lambda a,b: a-b,
           '*': lambda a,b: a*b, '/': lambda a,b: int(a/b)}
    
    for t in tokens:
        if t in ops:
            b, a = stack.pop(), stack.pop()
            stack.append(ops[t](a, b))
        else:
            stack.append(int(t))
    
    return stack[0]
```

### Min Stack
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
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()
    
    def top(self): return self.stack[-1]
    def getMin(self): return self.min_stack[-1]
```

### Largest Rectangle in Histogram
```python
def largest_rect(heights):
    stack = []
    max_area = 0
    heights.append(0)  # Sentinel
    
    for i, h in enumerate(heights):
        while stack and h < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    return max_area
```

### Simplify Path
```python
def simplify_path(path: str) -> str:
    stack = []
    for part in path.split('/'):
        if part == '..':
            if stack: stack.pop()
        elif part and part != '.':
            stack.append(part)
    return '/' + '/'.join(stack)
```

### Decode String (e.g., "3[a2[c]]" → "accaccacc")
```python
def decode_string(s: str) -> str:
    stack = []
    curr_str = ""
    curr_num = 0
    
    for c in s:
        if c.isdigit():
            curr_num = curr_num * 10 + int(c)
        elif c == '[':
            stack.append((curr_str, curr_num))
            curr_str, curr_num = "", 0
        elif c == ']':
            prev_str, num = stack.pop()
            curr_str = prev_str + curr_str * num
        else:
            curr_str += c
    
    return curr_str
```

---

## 📊 Complexity Reference

| Operation | Time | Space |
|-----------|------|-------|
| Push | O(1) | O(1) |
| Pop | O(1) | O(1) |
| Peek | O(1) | O(1) |
| Is Empty | O(1) | O(1) |
| Search | O(n) | O(1) |

---

## 🏷️ Pattern Recognition

| Keyword | Pattern |
|---------|---------|
| "valid parentheses" | Stack matching |
| "balanced brackets" | Stack matching |
| "next greater element" | Monotonic stack (increasing) |
| "next smaller element" | Monotonic stack (decreasing) |
| "days until warmer" | Monotonic stack |
| "largest rectangle" | Monotonic stack |
| "evaluate expression" | Two stacks or single stack |
| "decode/encode" | Stack for nested structure |
| "simplify path" | Stack for components |
| "undo operation" | Stack for history |

---

## 💡 Pro Tips

```python
# 1) Always check before popping
if stack:
    stack.pop()

# 2) For operators, pop order matters!
b = stack.pop()  # Second operand first
a = stack.pop()  # First operand second
result = a - b   # Correct order

# 3) Store indices, not values (for monotonic stack)
stack.append(i)  # Store index
nums[stack[-1]]  # Access value

# 4) Sentinel value trick
heights.append(0)  # Forces all remaining to pop
```

---

## ⚠️ Gotchas

```python
# 1) Empty stack access
stack.pop()      # ❌ Error if empty!
stack[-1]        # ❌ Error if empty!

# Safe version
if stack:
    val = stack.pop()

# 2) Integer division toward zero
int(-3 / 2)      # -2 in Python 3 (truncates toward 0)
-3 // 2          # -2 (floor division - different!)
```

---

> 📌 **Print this and keep it handy during practice!**
