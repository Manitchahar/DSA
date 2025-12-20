# 🧠 Greedy Algorithms Explained (For Beginners!)

> **No jargon. Just plain English explanations.**

---

## Table of Contents
1. [The "Greedy" Mental Model](#1-the-greedy-mental-model)
2. [Pattern 1: The "Reach" (Jump Game)](#2-pattern-1-the-reach-jump-game)
3. [Pattern 2: The "Partition" (Intervals)](#3-pattern-2-the-partition-partition-labels)
4. [Pattern 3: The "Delta" (Gas Station)](#4-pattern-3-the-delta-gas-station)

---

## 1. The "Greedy" Mental Model

### 📖 What is it?
Making the **best local choice** right now, and hoping it leads to the best global outcome.
"I'll eat the marshmallow now instead of waiting for two later."

### 🤔 The Catch
Greedy doesn't always work!
*   **Example where it fails:** Shortest path in a graph with weights. You might take a cheap road now that leads to a super expensive bridge later.
*   **Example where it works:** Buying things with the fewest coins (US currency). You take quarters first, then dimes...

### 🔑 When To Use It
*   **Keywords:** "Max usage", "Furthest Reach", "Earliest deadline".
*   Unfortunately, it's hard to prove. If "sorting" or "max heap" seems too slow, try Greedy.

---

## 2. Pattern 1: The "Reach" (Jump Game)

### 📖 What is it?
You want to see how far you can get. You keep updating your "Max Reach" as you iterate.

### 💡 The Visual
Indices: `0  1  2  3  4`
Values:  `2  3  1  1  4`

*   Start at 0. Value is 2. I can reach index `0 + 2 = 2`. **Max Reach = 2**.
*   Move to 1. Value is 3. I can reach index `1 + 3 = 4`. **Max Reach = 4**.
*   ...

### 💻 The Code

```python
def canJump(nums):
    goal = len(nums) - 1
    
    # Iterate backwards (Greedy: Can I reach the current goal?)
    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= goal:
            goal = i
            
    return goal == 0
```
*(Alternatively, iterate forward keeping track of `maxReach`)*

### 📺 Learn More
- [NeetCode - Jump Game](https://www.youtube.com/watch?v=Yan0cv2cLy8)

---

## 3. Pattern 2: The "Partition" (Partition Labels)

### 📖 What is it?
Splitting a string/array into chunks based on "last occurrence".

### 💡 The Intuition
String: `ababcbacadefegdehijhklij`
1.  See `a`. Last time `a` appears is index 8. So our chunk MUST go *at least* until 8.
2.  See `b`. Last `b` is at 5. 5 < 8, so our chunk end is still 8.
3.  ...
4.  Reach index 8. We are at the chunk end! **Cut!** Start new chunk.

### 💻 The Code

```python
def partitionLabels(s):
    # 1. Map each char to its last index
    lastIndex = {c: i for i, c in enumerate(s)}
    
    res = []
    size, end = 0, 0
    
    for i, c in enumerate(s):
        size += 1
        end = max(end, lastIndex[c])
        
        if i == end:
            res.append(size)
            size = 0
            
    return res
```

### 📺 Learn More
- [NeetCode - Partition Labels](https://www.youtube.com/watch?v=B7m8UmZE-vw)

---

## 4. Pattern 3: The "Delta" (Gas Station)

### 📖 What is it?
Tracking a running total. If it drops below zero, you know you started at the wrong place.

### 💡 The Intuition
*   `gas = [1, 2, 3, 4, 5]`
*   `cost = [3, 4, 5, 1, 2]`
*   `diff = [-2, -2, -2, 3, 3]`

If my tank goes negative, I couldn't have started at any station I just visited. Reset and try starting from the *next* one.

### 💻 The Code

```python
def canCompleteCircuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1
        
    total = 0
    start = 0
    
    for i in range(len(gas)):
        total += (gas[i] - cost[i])
        
        if total < 0:
            total = 0
            start = i + 1
            
    return start
```

### 📺 Learn More
- [NeetCode - Gas Station](https://www.youtube.com/watch?v=lJwbPZGo05A)

---

## 🎯 Quick Decision Guide

| Problem Type | Pattern |
|-------------|---------|
| "Can I reach the end?" | **Max Reach** (Jump Game) |
| "Min jumps to end" | **Implicit BFS** (Jump Game II) |
| "Split string unique chars" | **Last Index Map** |
| "Circular route", "Resources" | **Prefix Sum / Delta check** |
| "Merge intervals" | **Sort by start time** |

---
