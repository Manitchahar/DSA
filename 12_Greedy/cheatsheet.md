# 🚀 Greedy Cheat Sheet

---

## 🎯 When to Use Greedy

- Local optimal leads to global optimal
- Problems with clear "best choice" at each step
- Interval scheduling, activity selection

---

## Pattern Templates

### Interval Scheduling (Max Non-Overlapping)
```python
def max_intervals(intervals):
    intervals.sort(key=lambda x: x[1])  # Sort by END
    count, end = 0, float('-inf')
    for s, e in intervals:
        if s >= end:
            count += 1
            end = e
    return count
```

### Jump Game
```python
def can_jump(nums):
    max_reach = 0
    for i, jump in enumerate(nums):
        if i > max_reach: return False
        max_reach = max(max_reach, i + jump)
    return True
```

### Gas Station
```python
def gas_station(gas, cost):
    total = current = start = 0
    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total += diff
        current += diff
        if current < 0:
            start = i + 1
            current = 0
    return start if total >= 0 else -1
```

---

> 📌 Greedy = Sort first, then optimal choice at each step
