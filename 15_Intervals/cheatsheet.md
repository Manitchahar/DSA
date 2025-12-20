# 🚀 Intervals Cheat Sheet

---

## 🎯 Pattern Templates

### Merge Intervals
```python
def merge(intervals):
    intervals.sort()
    res = [intervals[0]]
    for s, e in intervals[1:]:
        if s <= res[-1][1]:
            res[-1][1] = max(res[-1][1], e)
        else:
            res.append([s, e])
    return res
```

### Insert Interval
```python
def insert(intervals, new):
    res = []
    for i, (s, e) in enumerate(intervals):
        if e < new[0]:
            res.append([s, e])
        elif s > new[1]:
            res.append(new)
            return res + intervals[i:]
        else:
            new = [min(s, new[0]), max(e, new[1])]
    res.append(new)
    return res
```

### Min Removals for Non-Overlapping
```python
def erase(intervals):
    intervals.sort(key=lambda x: x[1])  # Sort by END
    count, end = 0, float('-inf')
    for s, e in intervals:
        if s >= end:
            end = e
        else:
            count += 1
    return count
```

---

> 📌 Sort by START to merge, sort by END to select max non-overlapping
