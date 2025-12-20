# 🚀 Strings Cheat Sheet - Python

> Quick reference for interviews and problem-solving

---

## ⚡ Python String Operations

```python
# ═══════════════════════════════════════════════════════
# CREATION & BASICS
# ═══════════════════════════════════════════════════════
s = "hello"                 # String literal
s = 'hello'                 # Same thing
s = str(123)                # Convert to string
s = f"Value: {x}"           # f-string formatting
s = "".join(['a','b','c'])  # From list: "abc"

# ═══════════════════════════════════════════════════════
# ACCESS & SLICING
# ═══════════════════════════════════════════════════════
s[0]                # First char
s[-1]               # Last char
s[1:4]              # Slice [1,4) → "ell"
s[::-1]             # Reverse → "olleh"
s[::2]              # Every 2nd char

# ═══════════════════════════════════════════════════════
# SEARCHING
# ═══════════════════════════════════════════════════════
'el' in s           # True - substring check
s.find('el')        # 1 - index, or -1 if not found
s.rfind('l')        # 3 - from right
s.index('el')       # 1 - raises ValueError if not found
s.count('l')        # 2 - count occurrences

# ═══════════════════════════════════════════════════════
# MODIFICATION (returns new string)
# ═══════════════════════════════════════════════════════
s.replace('l', 'L')     # "heLLo"
s.upper()               # "HELLO"
s.lower()               # "hello"
s.capitalize()          # "Hello"
s.title()               # "Hello" (each word)
s.strip()               # Remove whitespace ends
s.lstrip()              # Remove left whitespace
s.rstrip()              # Remove right whitespace

# ═══════════════════════════════════════════════════════
# SPLITTING & JOINING
# ═══════════════════════════════════════════════════════
"a,b,c".split(',')      # ['a', 'b', 'c']
"hello world".split()   # ['hello', 'world']
','.join(['a','b'])     # "a,b"
' '.join(words)         # Join with space

# ═══════════════════════════════════════════════════════
# CHARACTER CHECKS
# ═══════════════════════════════════════════════════════
c.isalpha()         # Is letter?
c.isdigit()         # Is digit?
c.isalnum()         # Is alphanumeric?
c.islower()         # Is lowercase?
c.isupper()         # Is uppercase?
c.isspace()         # Is whitespace?

# ═══════════════════════════════════════════════════════
# ASCII CONVERSION
# ═══════════════════════════════════════════════════════
ord('a')            # 97 - char to ASCII
chr(97)             # 'a' - ASCII to char
ord('A')            # 65
ord('0')            # 48
```

---

## 🧰 Must-Know Python Tools

```python
from collections import Counter, defaultdict

# Frequency counting
freq = Counter("abracadabra")  # {'a': 5, 'b': 2, 'r': 2, ...}
freq.most_common(2)            # [('a', 5), ('b', 2)]

# Default dict for grouping
groups = defaultdict(list)
for word in words:
    groups[len(word)].append(word)

# Sorting string
sorted_s = ''.join(sorted(s))

# Check anagram
Counter(s1) == Counter(s2)
sorted(s1) == sorted(s2)
```

---

## 🎯 Pattern Templates

### Palindrome Check (Two Pointers)
```python
def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
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

### Sliding Window - Longest Substring Without Repeating
```python
def length_of_longest_substring(s: str) -> int:
    seen = {}
    left = max_len = 0
    for right, c in enumerate(s):
        if c in seen and seen[c] >= left:
            left = seen[c] + 1
        seen[c] = right
        max_len = max(max_len, right - left + 1)
    return max_len
```

### Sliding Window - Fixed Size (Anagram Finding)
```python
def find_anagrams(s: str, p: str) -> list:
    from collections import Counter
    result = []
    p_count = Counter(p)
    s_count = Counter()
    
    for i, c in enumerate(s):
        s_count[c] += 1
        if i >= len(p):
            left_char = s[i - len(p)]
            s_count[left_char] -= 1
            if s_count[left_char] == 0:
                del s_count[left_char]
        if s_count == p_count:
            result.append(i - len(p) + 1)
    return result
```

### String Reversal (In-Place for List)
```python
def reverse_string(s: list) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
```

### Reverse Words
```python
def reverse_words(s: str) -> str:
    return ' '.join(s.split()[::-1])
```

### Check Anagram
```python
def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
    # OR: return sorted(s) == sorted(t)
```

### Group Anagrams
```python
def group_anagrams(strs: list) -> list:
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())
```

### Longest Common Prefix
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

### String to Integer (atoi)
```python
def my_atoi(s: str) -> int:
    s = s.strip()
    if not s:
        return 0
    
    sign = 1
    i = 0
    if s[0] in ['-', '+']:
        sign = -1 if s[0] == '-' else 1
        i = 1
    
    result = 0
    while i < len(s) and s[i].isdigit():
        result = result * 10 + int(s[i])
        i += 1
    
    result *= sign
    return max(min(result, 2**31 - 1), -2**31)
```

---

## 📊 Complexity Reference

| Operation | Time | Space |
|-----------|------|-------|
| Index access `s[i]` | O(1) | O(1) |
| Concatenation `s + t` | O(n+m) | O(n+m) |
| Substring `s[a:b]` | O(b-a) | O(b-a) |
| Find/Search `s.find(p)` | O(n*m) | O(1) |
| Replace `s.replace()` | O(n) | O(n) |
| Split `s.split()` | O(n) | O(n) |
| Join `''.join(list)` | O(n) | O(n) |
| Sort `sorted(s)` | O(n log n) | O(n) |
| Reverse `s[::-1]` | O(n) | O(n) |

---

## 💡 Pro Tips

### 1. Efficient String Building
```python
# ❌ O(n²) - creates new string each time
result = ""
for c in chars:
    result += c

# ✅ O(n) - use list and join
result = []
for c in chars:
    result.append(c)
return "".join(result)
```

### 2. Character Frequency Array (Fixed Alphabet)
```python
# For lowercase letters only - faster than Counter
freq = [0] * 26
for c in s:
    freq[ord(c) - ord('a')] += 1
```

### 3. Sliding Window Key Insight
```python
# For fixed window, maintain state incrementally
# Add char entering window, remove char leaving window
```

### 4. Palindrome Tricks
```python
# Check if can form palindrome
# At most one char can have odd frequency
def can_form_palindrome(s):
    freq = Counter(s)
    odd_count = sum(1 for v in freq.values() if v % 2 == 1)
    return odd_count <= 1
```

---

## ⚠️ Gotchas

```python
# 1) Strings are IMMUTABLE
s = "hello"
s[0] = 'H'          # ❌ TypeError

# 2) Concatenation creates new string
s = s + "!"         # New string object created

# 3) Case sensitivity
"Hello".find("hello")  # -1 (not found!)
"Hello".lower().find("hello")  # 0 ✅

# 4) Empty string checks
if s:               # False if empty
    ...
if len(s) > 0:      # Same thing, less Pythonic
    ...

# 5) Whitespace in split
"  a  b  ".split()      # ['a', 'b'] - handles multiple spaces
"  a  b  ".split(' ')   # ['', '', 'a', '', 'b', '', '']
```

---

## 🏷️ Pattern Recognition

| Keyword | Pattern |
|---------|---------|
| "palindrome" | Two Pointers (both ends) |
| "anagram" | HashMap/Counter or Sorting |
| "substring without repeating" | Sliding Window + Set |
| "permutation of" | Sliding Window + Counter |
| "longest/shortest substring with..." | Sliding Window |
| "reverse string/words" | Two Pointers |
| "pattern matching" | KMP / Sliding Window |
| "encode/decode" | Usually simulation |
| "subsequence" | Two Pointers or DP |

---

> 📌 **Print this and keep it handy during practice!**
