# 🚀 Hash Tables Cheat Sheet - Python

> Quick reference for interviews

---

## ⚡ Dict Operations

```python
# Creation
d = {}
d = {'a': 1, 'b': 2}

# Access - O(1) average
d['a']                      # Get (KeyError if missing)
d.get('a')                  # Get (None if missing)
d.get('a', 0)               # Get with default

# Modify - O(1) average
d['c'] = 3                  # Set
d.setdefault('c', 3)        # Set only if missing
del d['a']                  # Delete
d.pop('a')                  # Delete and return

# Check
'a' in d                    # O(1)
len(d)                      # O(1)

# Iterate
for k in d:                 # Keys
for v in d.values():        # Values
for k, v in d.items():      # Both
```

## ⚡ Set Operations

```python
s = set()
s = {1, 2, 3}

s.add(x)            # Add
s.remove(x)         # Remove (error if missing)
s.discard(x)        # Remove (no error)
x in s              # Check O(1)

a | b               # Union
a & b               # Intersection
a - b               # Difference
```

## ⚡ Counter

```python
from collections import Counter

freq = Counter([1, 1, 2, 3])
freq[1]                     # 2
freq.most_common(2)         # [(1, 2), (3, 1)]
```

## ⚡ defaultdict

```python
from collections import defaultdict

d = defaultdict(int)        # 0 for missing
d = defaultdict(list)       # [] for missing
d[key] += 1                 # No KeyError!
```

---

## 🎯 Pattern Templates

### Two Sum
```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
```

### Frequency Count
```python
freq = Counter(nums)
# or
freq = {}
for x in nums:
    freq[x] = freq.get(x, 0) + 1
```

### Group By
```python
groups = defaultdict(list)
for item in items:
    groups[key(item)].append(item)
```

### Contains Duplicate
```python
def has_dup(nums):
    return len(nums) != len(set(nums))
```

### Subarray Sum = K
```python
def count_subarrays(nums, k):
    count = prefix = 0
    seen = {0: 1}
    for x in nums:
        prefix += x
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return count
```

---

## 🏷️ Pattern Recognition

| Keyword | Pattern |
|---------|---------|
| "pair sum" | HashMap complement |
| "frequency" | Counter |
| "group by" | defaultdict(list) |
| "duplicate" | Set |
| "subarray sum" | Prefix + HashMap |
| "unique" | Counter then filter |

---

> 📌 HashMap = O(1) lookup by key
