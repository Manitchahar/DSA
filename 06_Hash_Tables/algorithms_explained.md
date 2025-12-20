# 🧠 Hash Table Algorithms Explained (For Beginners!)

> **No jargon. Just plain English explanations.**

---

## Table of Contents
1. [The "Hash Table" Mental Model](#1-the-hash-table-mental-model)
2. [The "Two Sum" Pattern](#2-the-two-sum-pattern-look-back)
3. [Frequency Counting](#3-frequency-counting)
4. [Grouping / Bucketing](#4-grouping--bucketing)

---

## 1. The "Hash Table" Mental Model

### 📖 What is it?
A magical book where you can find any page instantly if you know the title. No need to flip through pages.

*   **Map (Dict):** Key -> Value
*   **Set:** Key (just existence)

### 🤔 The Problem It Solves
"Does X exist in this list?"
*   **Without Hash Table (Array):** You have to check every single item. O(n).
*   **With Hash Table:** You jump straight to the answer. O(1).

### 💡 The Visual

```
Array: [?, ?, ?, "Apple", ?]
check("Apple"):
  Is index 0 Apple? No.
  Is index 1 Apple? No.
  ...
  Is index 3 Apple? Yes! -> Found in 4 steps.

HashMap:
  "Orange" -> Slot 1
  "Apple"  -> Slot 242
  "Banana" -> Slot 55
  
check("Apple"):
  Hash("Apple") = 242. 
  Go to Slot 242. 
  Is it there? Yes! -> Found in 1 step.
```

### 💻 Python Basics

```python
# Dictionary (Key -> Value)
my_dict = {"name": "Alice", "age": 25}
val = my_dict["name"]    # O(1)
exists = "age" in my_dict # O(1)

# Set (Unique Keys only)
my_set = {1, 2, 3}
my_set.add(4)
exists = 4 in my_set     # O(1)
```

---

## 2. The "Two Sum" Pattern (Look Back)

### 📖 What is it?
Instead of checking "Does A + B = Target" by trying every pair (O(n²)), we check "Have I realized what looking for?"

### 💡 The Intuition
Target = 9.
I am running through the numbers.
I see a `7`.
I ask: "Have I seen a `2` before?" (Since 9 - 7 = 2).
*   If **Yes**: I found the pair! `(2, 7)`
*   If **No**: I write `7` down in my notebook (Hash Map) and keep going.

### 💻 The Code

```python
def twoSum(nums, target):
    prevMap = {}  # val -> index
    
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
```

### 📺 Learn More
- [NeetCode - Two Sum](https://www.youtube.com/watch?v=KLlXCFG5TnA)

---

## 3. Frequency Counting

### 📖 What is it?
Counting how many times things appear.

### 🤔 The Problem It Solves
*   "Is this string an anagram of that one?" (Do they have same letter counts?)
*   "Find the most frequent element."

### 💻 The Code
Python's `Counter` is your best friend.

```python
from collections import Counter

s = "banana"
counts = Counter(s)
# {'a': 3, 'n': 2, 'b': 1}
```

**Anagram Check:**
```python
return Counter(s) == Counter(t)
```

### 📺 Learn More
- [NeetCode - Valid Anagram](https://www.youtube.com/watch?v=9UtInBqnCgA)

---

## 4. Grouping / Bucketing

### 📖 What is it?
Grouping items together that share a common "key" or property.

### 🤔 The Problem It Solves
"Group all anagrams together."
`["eat", "tea", "tan", "ate", "nat", "bat"]`
-> `[["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]`

### 💡 The Intuition
We need a **Key** that is the same for all items in the group.
*   For anagrams, the sorted version of the word is the same!
*   `"eat"` -> `"aet"`
*   `"tea"` -> `"aet"`

### 💻 The Code

```python
from collections import defaultdict

def groupAnagrams(strs):
    groups = defaultdict(list)
    
    for s in strs:
        # List cannot be key, so use tuple
        key = tuple(sorted(s)) 
        groups[key].append(s)
        
    return list(groups.values())
```

### 📺 Learn More
- [NeetCode - Group Anagrams](https://www.youtube.com/watch?v=vzdNOK2oB2E)

---

## 🎯 Quick Decision Guide

| Problem Type | Pattern |
|-------------|---------|
| "Find pair with sum X" | **Two Sum** (Map of Seen Values) |
| "Does X exist?", "Duplicates" | **HashSet** |
| "Most frequent", "Anagrams" | **HashMap / Counter** |
| "Subarray Sum equals K" | **Prefix Sum + HashMap** |
| "Group by property" | **HashMap (Key -> List)** |

---
