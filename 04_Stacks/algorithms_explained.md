# 🧠 Stack Algorithms Explained (For Beginners!)

> **No jargon. Just plain English explanations.**

---

## Table of Contents
1. [The "Stack" Mental Model](#1-the-stack-mental-model)
2. [Valid Parentheses Pattern](#2-valid-parentheses-pattern)
3. [Monotonic Stack Pattern](#3-monotonic-stack-pattern)
4. [Expression Evaluation Pattern](#4-expression-evaluation-pattern)

---

## 1. The "Stack" Mental Model

### 📖 What is it?
A LIFO (Last-In, First-Out) data structure. The last thing you put in is the *first* thing you take out.

### 🤔 The Real World Analogy
*   **The Dirty Plate Stack:** You wash the top plate first (the one you placed there last). You can't safely grab a plate from the bottom.
*   **Browser Back Button:** You go from Site A -> Site B -> Site C. Pressing "Back" takes you to B, then A. It remembers your history in reverse order.

### 💡 The Visual

```
       |     |
Push 3 | [3] | Top
       | [2] |
       | [1] | Bottom
       -------
       
Pop!   -> Returns 3
       |     |
       |     | 
       | [2] | Top
       | [1] | Bottom
       -------
```

### 🔑 When To Use It
*   **Keywords:** "Reverse", "Match", "Backtrack", "Most recent", "Nested".
*   **You need to:** Process data in the opposite order of arrival, or pairs things up (like matching socks).

### 💻 Python Basics
In Python, just use a **list**!
*   `stack.append(x)` = Push
*   `stack.pop()` = Pop
*   `stack[-1]` = Peek (Look at top)

---

## 2. Valid Parentheses Pattern

### 📖 What is it?
Ensuring that every opening bracket like `(`, `{`, `[` has a matching closing bracket in the correct order.

### 🤔 The Problem It Solves
*   Syntax checking in compilers (did you close that function?).
*   Validating math expressions.

### 💡 The Intuition
Imagine a game of Tetris.
*   Opening bracket `(` falls down. It stays there waiting.
*   Closing bracket `)` falls down. It destroys the matching `(` at the *top* of the pile.
*   If the wrong shape falls (e.g., `]` on top of `(`), Game Over.
*   If the pile is empty at the end, You Win!

### 💻 The Code

```python
def isValid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in mapping:
            # It's a closing bracket
            # Check if stack is not empty AND top matches
            if stack and stack[-1] == mapping[char]:
                stack.pop()
            else:
                return False
        else:
            # It's an opening bracket
            stack.append(char)
            
    return not stack  # True if stack is empty
```

### 📺 Learn More
- [NeetCode - Valid Parentheses](https://www.youtube.com/watch?v=WTzjTskDFMg)

---

## 3. Monotonic Stack Pattern

### 📖 What is it?
A stack where elements are always sorted (either increasing or decreasing). We enforce this by popping elements that break the rule.

### 🤔 The Problem It Solves
"Find the **Next Greater Element**" or "Find the **Previous Smaller Element**".
Example: For `[2, 1, 5, 6, 2, 3]`, find the first number to the right that is bigger than the current one.

### 💡 The Intuition
Imagine a line of people sorted by height.
A giant walks in. He blocks the view for everyone shorter than him who came before.
*   If a new element is **smaller**, push it (it doesn't block anyone).
*   If a new element is **bigger**, it "pops" (resolves) all the smaller elements previously on the stack because it is their "next greater" element.

```
Array: [2, 1, 5]

1. Push 2. Stack: [2]
2. Push 1. Stack: [2, 1] (Decreasing order kept)
3. See 5. 
   - 5 is bigger than 1. So 5 is 1's "Next Greater". Pop 1.
   - 5 is bigger than 2. So 5 is 2's "Next Greater". Pop 2.
   - Push 5. Stack: [5]
```

### 💻 The Code (Daily Temperatures)

```python
def dailyTemperatures(temperatures: list) -> list:
    res = [0] * len(temperatures)
    stack = []  # pair: [temp, index]
    
    for i, t in enumerate(temperatures):
        # Whilst the current temp is warmer than the top of stack
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            res[stackInd] = i - stackInd  # Calculate distance
        stack.append([t, i])
        
    return res
```

### 📺 Learn More
- [NeetCode - Daily Temperatures](https://www.youtube.com/watch?v=cTBiBSnjO3c)

---

## 4. Expression Evaluation Pattern

### 📖 What is it?
Solving math expressions like `(1 + (4 + 5 + 2) - 3) + (6 + 8)`. Note the nesting!

### 🤔 The Problem It Solves
Calculators, script interpreters.

### 💡 The Intuition
Treat it like unboxing gifts.
1.  Keep putting numbers and `+` signs in your bag (Stack).
2.  When you see `(`, start a new mini-bag.
3.  When you see `)`, close the mini-bag, sum it up, and put the *result* back into the main bag.

### 💻 The Code (Reverse Polish Notation)
`["2","1","+","3","*"]` -> `((2 + 1) * 3)` -> `9`

```python
def evalRPN(tokens: list) -> int:
    stack = []
    for t in tokens:
        if t == "+":
            stack.append(stack.pop() + stack.pop())
        elif t == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a) # Order matters
        elif t == "*":
            stack.append(stack.pop() * stack.pop())
        elif t == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        else:
            stack.append(int(t))
    return stack[0]
```

### 📺 Learn More
- [NeetCode - Evaluate Reverse Polish Notation](https://www.youtube.com/watch?v=iu0082c4HDE)

---

## 🎯 Quick Decision Guide

| Problem Type | Pattern |
|-------------|---------|
| "Valid Parentheses", "Match" | **Basic Matching** |
| "Next Greater", "Daily Temps", "Stock Span" | **Monotonic Stack** |
| "Evaluate Expression", "Calculator" | **Stack for results** |
| "Decode String", "Flatten", "Unix Path" | **Stack for context** |
| "Min Stack" | **Two Stacks** (one for values, one for mins) |

---
