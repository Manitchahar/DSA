# 📚 Intervals - DSA Guide

> **Master overlapping ranges!**

---

## 🎨 Common Patterns

### Merge Intervals

```python
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    
    return merged
```

### Insert Interval

```python
def insert(intervals, new):
    result = []
    for i, (start, end) in enumerate(intervals):
        if end < new[0]:
            result.append([start, end])
        elif start > new[1]:
            result.append(new)
            return result + intervals[i:]
        else:
            new = [min(start, new[0]), max(end, new[1])]
    result.append(new)
    return result
```

### Non-Overlapping Intervals (Min Removals)

```python
def erase_overlap(intervals):
    intervals.sort(key=lambda x: x[1])
    count = 0
    end = float('-inf')
    
    for s, e in intervals:
        if s >= end:
            end = e
        else:
            count += 1
    
    return count
```

---

## 🎯 LeetCode Problems

| # | Problem | 📺 Video |
|---|---------|----------|
| 56 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | [NeetCode](https://youtu.be/44H3cEC2fFM) |
| 57 | [Insert Interval](https://leetcode.com/problems/insert-interval/) | [NeetCode](https://youtu.be/A8NUOmlwOlM) |
| 435 | [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | [NeetCode](https://youtu.be/nONCGxWoUfM) |
| 252 | Meeting Rooms | [NeetCode](https://youtu.be/PaJxqZVPhbg) |
| 253 | Meeting Rooms II | [NeetCode](https://youtu.be/FdzJmTCVyJU) |
| 1851 | [Min Interval to Include Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/) | Advanced |

---

> 💡 Sort by start OR end depending on the problem!
