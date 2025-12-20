# 🚀 Recursion & Backtracking Cheat Sheet

---

## 🎯 Backtracking Template

```python
def backtrack(path, choices):
    if is_solution(path):
        result.append(path[:])
        return
    
    for choice in choices:
        if is_valid(choice):
            path.append(choice)
            backtrack(path, remaining)
            path.pop()  # Undo
```

---

## 🎯 Common Patterns

### Subsets
```python
def subsets(nums):
    res = []
    def bt(i, path):
        res.append(path[:])
        for j in range(i, len(nums)):
            path.append(nums[j])
            bt(j + 1, path)
            path.pop()
    bt(0, [])
    return res
```

### Permutations
```python
def permutations(nums):
    res = []
    def bt(path, used):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                bt(path, used)
                path.pop()
                used[i] = False
    bt([], [False]*len(nums))
    return res
```

### Combinations
```python
def combine(n, k):
    res = []
    def bt(start, path):
        if len(path) == k:
            res.append(path[:])
            return
        for i in range(start, n+1):
            path.append(i)
            bt(i+1, path)
            path.pop()
    bt(1, [])
    return res
```

---

## 🏷️ Pattern Recognition

| Type | Key Difference |
|------|----------------|
| Subsets | All combinations of any size |
| Permutations | Order matters, use all |
| Combinations | Order doesn't matter, pick k |

---

> 📌 Always copy path when adding to result!
