# 📚 Strings - Complete DSA Guide (Python)

> **Master string manipulation for coding interviews!**

---

## 🎯 What You'll Master

- String fundamentals and Python specifics
- Time & Space complexity for all operations
- Essential patterns: Two Pointers, Sliding Window, Palindromes
- 30+ curated LeetCode problems
- Pro tips, tricks, and common pitfalls

---

## ✅ How To Use This Folder

1. **Learn the concept** (read this README)
2. **Memorize the templates** (see `cheatsheet.md`)
3. **Understand algorithms** (see `algorithms_explained.md`)
4. **Grind LeetCode** (see `leetcode_problems.md`)
5. **Practice in** `solutions/` folder

---

## 📖 Table of Contents

1. [Fundamentals](#-fundamentals)
2. [Python String Internals](#-python-string-internals)
3. [Core Operations & Complexity](#-core-operations--complexity)
4. [Essential Patterns](#-essential-patterns)
5. [Common Pitfalls](#-common-pitfalls)
6. [Mastery Checklist](#-mastery-checklist)

---

## 🔥 Fundamentals

### What is a String?

A **string** is a sequence of characters. In Python, strings are **immutable** - once created, they cannot be modified.

```python
s = "hello"
# s[0] = 'H'  # ❌ TypeError! Strings are immutable

# ✅ Create a new string instead
s = 'H' + s[1:]  # "Hello"
```

### Key Properties

| Property | Description |
|----------|-------------|
| **Immutable** | Cannot modify in-place (must create new string) |
| **Indexed** | O(1) access via index |
| **Iterable** | Can loop through characters |
| **Unicode** | Python 3 strings are Unicode by default |

---

## 🐍 Python String Internals

### String Interning

Python caches small strings for efficiency:

```python
a = "hello"
b = "hello"
print(a is b)  # True - same object in memory!

# But not for computed strings
c = "hel" + "lo"
print(a is c)  # True (optimizer caught it)

d = "".join(['h', 'e', 'l', 'l', 'o'])
print(a is d)  # May be False
```

### Immutability Implications

```python
# ❌ Inefficient - O(n²) for n concatenations
s = ""
for c in chars:
    s += c  # Creates new string each time!

# ✅ Efficient - O(n)
s = "".join(chars)

# ✅ Also efficient - list then join
result = []
for c in chars:
    result.append(c)
s = "".join(result)
```

### Essential String Tools

```python
# Character operations
ord('a')       # 97 - ASCII value
chr(97)        # 'a' - character from ASCII

# Check character type
c.isalpha()    # Is letter?
c.isdigit()    # Is digit?
c.isalnum()    # Is alphanumeric?
c.islower()    # Is lowercase?
c.isupper()    # Is uppercase?
c.isspace()    # Is whitespace?

# Case conversion
s.lower()      # "HELLO" → "hello"
s.upper()      # "hello" → "HELLO"
s.capitalize() # "hello" → "Hello"
s.title()      # "hello world" → "Hello World"
s.swapcase()   # "HeLLo" → "hEllO"

# Searching
s.find(sub)    # Index of sub, or -1
s.rfind(sub)   # From right
s.index(sub)   # Like find, but raises ValueError
s.count(sub)   # Count occurrences

# Modification (returns new string)
s.replace(old, new)
s.strip()      # Remove whitespace from ends
s.lstrip()     # Remove from left
s.rstrip()     # Remove from right

# Splitting and Joining
s.split()           # Split by whitespace
s.split(',')        # Split by comma
','.join(list)      # Join list with comma
s.splitlines()      # Split by newlines

# Checking content
s.startswith(prefix)
s.endswith(suffix)
```

---

## ⚡ Core Operations & Complexity

### Time Complexity

| Operation | Time | Notes |
|-----------|------|-------|
| `s[i]` Access | O(1) | Index lookup |
| `len(s)` | O(1) | Stored value |
| `s + t` Concatenate | O(n + m) | Creates new string |
| `s * k` Repeat | O(n * k) | Creates new string |
| `c in s` | O(n) | Linear search |
| `s.find(t)` | O(n * m) | Naive search |
| `s.replace(a, b)` | O(n) | Scans entire string |
| `s.split()` | O(n) | |
| `''.join(list)` | O(n) | Total characters |
| `s == t` | O(min(n,m)) | Compare characters |
| `s[a:b]` Slice | O(b - a) | Creates copy |
| `sorted(s)` | O(n log n) | |

### Space Complexity

| Operation | Space |
|-----------|-------|
| Most string ops | O(n) - creates new string |
| `s[i]` access | O(1) |
| Slice `s[a:b]` | O(b - a) |

---

## 🎨 Essential Patterns

### 1️⃣ Two Pointers (Palindrome Check)

```python
def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        # Skip non-alphanumeric
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
```

### 2️⃣ Sliding Window (Substring Problems)

```python
def longest_substring_without_repeating(s: str) -> int:
    """Find length of longest substring without repeating chars"""
    char_index = {}  # char -> last seen index
    max_len = 0
    left = 0
    
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1  # Move left past duplicate
        char_index[char] = right
        max_len = max(max_len, right - left + 1)
    
    return max_len
```

### 3️⃣ HashMap (Anagram Detection)

```python
from collections import Counter

def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

def group_anagrams(strs: list) -> list:
    groups = {}
    for s in strs:
        key = tuple(sorted(s))  # Or use Counter as key
        groups.setdefault(key, []).append(s)
    return list(groups.values())
```

### 4️⃣ Two Pointers (String Reversal)

```python
def reverse_string(s: list) -> None:
    """In-place reversal (for char array)"""
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

def reverse_words(s: str) -> str:
    """Reverse word order"""
    return ' '.join(s.split()[::-1])
```

### 5️⃣ Prefix/Suffix Matching

```python
def longest_common_prefix(strs: list) -> str:
    if not strs:
        return ""
    
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
```

### 6️⃣ String Building (Efficient Concatenation)

```python
# ❌ Bad - O(n²)
result = ""
for char in chars:
    result += char

# ✅ Good - O(n)
result = []
for char in chars:
    result.append(char)
return "".join(result)

# ✅ Also good - list comprehension
result = "".join([process(c) for c in chars])
```

---

## 🧠 Problem-Solving Framework

### Pattern Recognition

| Keyword | Pattern |
|---------|---------|
| "Palindrome" | Two Pointers (outside-in) |
| "Anagram" | HashMap / Sorting |
| "Substring" | Sliding Window |
| "Subsequence" | Two Pointers / DP |
| "Permutation" | Sliding Window + HashMap |
| "Longest/Shortest with condition" | Sliding Window |
| "All substrings" | Usually O(n²) nested loops |
| "Pattern matching" | KMP / Rabin-Karp |

---

## ⚠️ Common Pitfalls

### 1. String Immutability

```python
# ❌ This doesn't work
s = "hello"
s[0] = 'H'  # TypeError!

# ✅ Convert to list, modify, join back
chars = list(s)
chars[0] = 'H'
s = ''.join(chars)
```

### 2. Concatenation in Loops

```python
# ❌ O(n²) - creates new string each iteration
for c in chars:
    s += c

# ✅ O(n) - use join
s = ''.join(chars)
```

### 3. Off-by-One in Slicing

```python
s = "hello"
s[0:5]   # "hello" - end is exclusive
s[:5]    # "hello" - same
s[0:-1]  # "hell" - -1 means stop before last
s[:]     # "hello" - full copy
```

### 4. Case Sensitivity

```python
# ❌ Might miss matches
if s.find("hello") != -1:
    ...

# ✅ Normalize case first
if s.lower().find("hello") != -1:
    ...
```

### 5. Empty String Edge Cases

```python
# Always check!
if not s:
    return result_for_empty

# Or handle in logic
for i, c in enumerate(s):  # Safe - empty string = no iterations
    ...
```

---

## 🧪 Required Drills

You should be able to code each in **≤ 10 minutes**:

- [ ] Check if string is palindrome (with/without ignoring non-alphanumeric)
- [ ] Reverse a string (in-place for char array)
- [ ] Reverse words in a sentence
- [ ] Check if two strings are anagrams
- [ ] Find first non-repeating character
- [ ] Longest substring without repeating characters
- [ ] Valid parentheses (using stack)
- [ ] String to integer (atoi)
- [ ] Group anagrams
- [ ] Longest common prefix

---

## 🏁 Mastery Checklist

- [ ] I understand why string concatenation in loops is O(n²)
- [ ] I can use `''.join()` efficiently
- [ ] I can apply sliding window to substring problems
- [ ] I can use HashMap for anagram problems
- [ ] I handle edge cases: empty string, single char, all same chars
- [ ] I know when to use two pointers vs sliding window
- [ ] I can convert between string and char array when needed

---

## 📁 Directory Structure

```
02_Strings/
├── README.md              # This file
├── cheatsheet.md          # Quick reference
├── algorithms_explained.md # Deep dives
├── leetcode_problems.md   # Curated problems
└── solutions/             # Your practice code
    ├── two_pointers/
    ├── sliding_window/
    ├── anagrams/
    └── palindromes/
```

---

## 🚀 Next Steps

1. Read the [Cheat Sheet](./cheatsheet.md)
2. Study [Algorithms Explained](./algorithms_explained.md)
3. Practice [LeetCode Problems](./leetcode_problems.md)

---

> 💡 **Pro Tip:** Always ask "Is the string sorted?" and "Do I need the actual substring or just its length?" These change your approach!

Happy Coding! 🎯
