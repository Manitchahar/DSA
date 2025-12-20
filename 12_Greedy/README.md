# 📚 Greedy Algorithms - DSA Guide

> **Make locally optimal choices for globally optimal solution!**

---

## 🔥 When Does Greedy Work?

1. **Greedy choice property:** Local optimal leads to global optimal
2. **Optimal substructure:** Problem can be broken down

---

## 🎨 Common Patterns

### Interval Scheduling

```python
def max_non_overlapping_intervals(intervals):
    intervals.sort(key=lambda x: x[1])  # Sort by end time
    count = 0
    end = float('-inf')
    
    for start, finish in intervals:
        if start >= end:
            count += 1
            end = finish
    
    return count
```

### Jump Game

```python
def can_jump(nums):
    max_reach = 0
    for i, jump in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + jump)
    return True
```

### Gas Station

```python
def can_complete_circuit(gas, cost):
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

## 🎯 LeetCode Problems

| # | Problem | 📺 Video |
|---|---------|----------|
| 55 | [Jump Game](https://leetcode.com/problems/jump-game/) | [NeetCode](https://youtu.be/Yan0cv2cLy8) |
| 45 | [Jump Game II](https://leetcode.com/problems/jump-game-ii/) | [NeetCode](https://youtu.be/dJ7sWiOoK7g) |
| 134 | [Gas Station](https://leetcode.com/problems/gas-station/) | [NeetCode](https://youtu.be/lJwbPZGo05A) |
| 846 | [Hand of Straights](https://leetcode.com/problems/hand-of-straights/) | [NeetCode](https://youtu.be/amnrMCVd2YI) |
| 1899 | [Merge Triplets](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) | [NeetCode](https://youtu.be/kShkQLQZ9K4) |
| 763 | [Partition Labels](https://leetcode.com/problems/partition-labels/) | [NeetCode](https://youtu.be/B7m8UmZE-vw) |
| 678 | [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) | [NeetCode](https://youtu.be/QhPdNS143Qg) |

---

> 💡 Greedy = sort first, then make best choice at each step!
