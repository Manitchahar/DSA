# 🧠 Intervals Explained (For Beginners!)

> **No jargon. Just plain English explanations.**

---

## Table of Contents
1. [The "Interval" Mental Model](#1-the-interval-mental-model)
2. [Pattern 1: Merge Intervals](#2-pattern-1-merge-intervals)
3. [Pattern 2: Non-Overlapping (Greedy)](#3-pattern-2-non-overlapping-greedy)
4. [Pattern 3: Sweep Line (Meeting Rooms II)](#4-pattern-3-sweep-line-meeting-rooms-ii)

---

## 1. The "Interval" Mental Model

### 📖 What is it?
A span of time or numbers with a `start` and `end`. `[1, 5]`.

### The Golden Rule
**ALWAYS SORT BY START TIME**.
If the intervals are sorted `[1, 3], [2, 6], [8, 10]`, it becomes incredibly easy to spot overlaps. You only need to compare the "current" interval with the "previous" one.

### 💡 Visualizing Overlaps
Given `A = [1, 5]`. Let's check `B`.
1.  **No Overlap:** `B = [6, 10]` (B starts after A ends).
2.  **Overlap:** `B = [2, 4]` (B starts before A ends).
    *   Condition: `B.start <= A.end`.

---

## 2. Pattern 1: Merge Intervals

### 📖 What is it?
combining `[1, 3]` and `[2, 6]` into `[1, 6]`.

### 💡 The Logic
1.  Sort the list.
2.  Take the first interval as `current`.
3.  Loop through the rest:
    *   If `next.start <= current.end`: **Merge!**
        *   `current.end = max(current.end, next.end)`
    *   Else: No overlap. Push `current` to result, set `current = next`.

### 💻 The Code

```python
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    output = [intervals[0]]
    
    for start, end in intervals[1:]:
        lastEnd = output[-1][1]
        
        if start <= lastEnd:
            # Merge: Extend the end of the last interval
            output[-1][1] = max(lastEnd, end)
        else:
            # No overlap: Add new interval
            output.append([start, end])
            
    return output
```

### 📺 Learn More
- [NeetCode - Merge Intervals](https://www.youtube.com/watch?v=44H3cEC2fFM)

---

## 3. Pattern 2: Non-Overlapping (Greedy)

### 📖 What is it?
"Remove the minimum number of intervals to make the rest non-overlapping."

### 💡 The Intuition
If two intervals overlap, **which one should I delete?**
*   `[1, 100]`
*   `[1, 2]`
If I keep `[1, 100]`, it blocks everything until 100.
If I keep `[1, 2]`, I free up time starting at 2.
**Greedy Strategy:** Always remove the one that **ends later**. (Keep the one that finishes earliest!)

### 💻 The Code

```python
def eraseOverlapIntervals(intervals):
    intervals.sort() # Sort by start
    res = 0
    prevEnd = intervals[0][1]
    
    for start, end in intervals[1:]:
        if start >= prevEnd:
            # No overlap, update end
            prevEnd = end
        else:
            # Overlap! Remove the one ending later 
            # (aka keep min end)
            res += 1
            prevEnd = min(prevEnd, end)
            
    return res
```

### 📺 Learn More
- [NeetCode - Non-overlapping Intervals](https://www.youtube.com/watch?v=nONCGxWoUfM)

---

## 4. Pattern 3: Sweep Line (Meeting Rooms II)

### 📖 What is it?
"How many rooms do we need?" (Maximum simultaneous meetings).

### 💡 The Intuition
Treat "Start time" as +1 room needed.
Treat "End time" as -1 room needed.
Sort ALL events together and sweep through time using a counter.

### 💻 The Code

```python
def minMeetingRooms(intervals):
    starts = sorted([i[0] for i in intervals])
    ends = sorted([i[1] for i in intervals])
    
    res, count = 0, 0
    s, e = 0, 0
    
    while s < len(intervals):
        if starts[s] < ends[e]:
            count += 1
            s += 1
        else:
            count -= 1
            e += 1
        res = max(res, count)
        
    return res
```

### 📺 Learn More
- [NeetCode - Meeting Rooms II](https://www.youtube.com/watch?v=FdzJmTCVyJU)

---

## 🎯 Quick Decision Guide

| Problem Type | Pattern |
|-------------|---------|
| "Combine overlapping" | **Sort + Merge** |
| "Insert new interval" | **Left part + Merge + Right part** |
| "Max non-overlapping" | **Sort + Greedy (Remove max end)** |
| "Simultaneous events" | **Sweep Line** (Count starts/ends) |

---
