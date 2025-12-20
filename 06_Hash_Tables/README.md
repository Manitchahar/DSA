# 📚 Hash Tables - Complete DSA Guide (Python)

> **Master the O(1) lookup data structure!**

---

## 🎯 What You'll Master

- Hash table fundamentals and collision handling
- Python dict and set operations
- Essential patterns: Two Sum, Frequency Counting, Grouping
- 20+ curated LeetCode problems

---

## 🔥 Fundamentals

### What is a Hash Table?

A **hash table** maps keys to values using a **hash function**. It provides average O(1) lookup, insert, and delete!

```
Key "apple" → hash("apple") = 42 → bucket[42] = "fruit"
Key "banana" → hash("banana") = 17 → bucket[17] = "yellow"

Lookup "apple":
1. hash("apple") = 42
2. bucket[42] = "fruit" ✓
```

### Key Properties

| Property | Description |
|----------|-------------|
| **O(1) Average** | Lookup, insert, delete |
| **O(n) Worst** | Many collisions |
| **Unordered** | No guaranteed order |
| **Unique Keys** | Each key appears once |

---

## 🐍 Python Implementation

### Dictionary (dict)

```python
# Creation
d = {}
d = {'a': 1, 'b': 2}
d = dict(a=1, b=2)

# Access
d['a']              # Get value (KeyError if missing)
d.get('a')          # Get value (None if missing)
d.get('a', 0)       # Get value (0 if missing)

# Modify
d['c'] = 3          # Add or update
d.update({'d': 4})  # Merge another dict
del d['a']          # Delete key
d.pop('b')          # Delete and return value

# Check
'a' in d            # Key exists?
len(d)              # Number of keys

# Iterate
for key in d:                   # Keys
for value in d.values():        # Values
for key, value in d.items():    # Both
```

### Set

```python
# Creation
s = set()
s = {1, 2, 3}

# Modify
s.add(4)            # Add element
s.remove(4)         # Remove (KeyError if missing)
s.discard(4)        # Remove (no error if missing)
s.pop()             # Remove and return arbitrary element

# Operations
a | b               # Union
a & b               # Intersection
a - b               # Difference
a ^ b               # Symmetric difference

# Check
4 in s              # Membership O(1)
```

### Counter

```python
from collections import Counter

# Count frequencies
freq = Counter([1, 1, 2, 3, 3, 3])
# Counter({3: 3, 1: 2, 2: 1})

freq[1]             # Get count: 2
freq.most_common(2) # Top 2: [(3, 3), (1, 2)]
```

### defaultdict

```python
from collections import defaultdict

# Auto-initialize missing keys
d = defaultdict(int)   # Missing key → 0
d = defaultdict(list)  # Missing key → []
d = defaultdict(set)   # Missing key → set()

# No need to check if key exists
d[key] += 1            # Works even if key is new
d[key].append(val)     # Works even if key is new
```

---

## ⚡ Core Operations & Complexity

| Operation | Average | Worst |
|-----------|---------|-------|
| Get `d[k]` | O(1) | O(n) |
| Set `d[k] = v` | O(1) | O(n) |
| Delete `del d[k]` | O(1) | O(n) |
| `k in d` | O(1) | O(n) |
| Iterate | O(n) | O(n) |

---

## 🎨 Essential Patterns

### 1️⃣ Two Sum Pattern

```python
def two_sum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

### 2️⃣ Frequency Counting

```python
from collections import Counter

def top_k_frequent(nums, k):
    freq = Counter(nums)
    return [x for x, _ in freq.most_common(k)]
```

### 3️⃣ Group By Key (Anagrams)

```python
def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())
```

### 4️⃣ Seen/Visited Tracking

```python
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

### 5️⃣ Prefix Sum + HashMap

```python
def subarray_sum_k(nums, k):
    count = 0
    prefix = 0
    seen = {0: 1}
    
    for num in nums:
        prefix += num
        if prefix - k in seen:
            count += seen[prefix - k]
        seen[prefix] = seen.get(prefix, 0) + 1
    
    return count
```

### 6️⃣ Index Mapping

```python
def first_unique_char(s):
    freq = Counter(s)
    for i, c in enumerate(s):
        if freq[c] == 1:
            return i
    return -1
```

---

## 🧠 Pattern Recognition

| Keyword | Pattern |
|---------|---------|
| "find pair with sum" | HashMap (complement lookup) |
| "frequency/count" | Counter |
| "group by property" | defaultdict(list) |
| "contains duplicate" | Set |
| "subarray sum = k" | Prefix sum + HashMap |
| "first unique" | Counter → scan |
| "isomorphic/bijection" | Two HashMaps |

---

## ⚠️ Common Pitfalls

### 1. KeyError
```python
# ❌ Crashes if key missing
value = d[key]

# ✅ Safe
value = d.get(key, default)
```

### 2. Modifying while iterating
```python
# ❌ RuntimeError
for key in d:
    del d[key]

# ✅ Iterate over copy
for key in list(d.keys()):
    del d[key]
```

### 3. Mutable keys
```python
# ❌ Lists can't be dict keys
d[[1, 2]] = "value"

# ✅ Use tuples
d[(1, 2)] = "value"
```

---

## 🏁 Mastery Checklist

- [ ] I use `get()` or `defaultdict` to avoid KeyError
- [ ] I use Counter for frequency problems
- [ ] I can solve Two Sum pattern instantly
- [ ] I know when to use dict vs set
- [ ] I understand prefix sum + hashmap pattern

---

## 📁 Directory Structure

```
06_Hash_Tables/
├── README.md
├── cheatsheet.md
├── algorithms_explained.md
├── leetcode_problems.md
└── solutions/
    ├── two_sum/
    ├── frequency/
    └── grouping/
```

---

> 💡 **Pro Tip:** When you need O(1) lookup by some key, think HashMap!

Happy Coding! 🎯
