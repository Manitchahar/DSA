# 🧠 String Algorithms Explained (For Beginners!)

> **No jargon. Just plain English explanations.**

---

## Table of Contents
1. [Sliding Window on Strings](#1-sliding-window-on-strings)
2. [Two Pointers for Strings](#2-two-pointers-for-strings)
3. [Anagram Detection](#3-anagram-detection)
4. [Palindrome Patterns](#4-palindrome-patterns)
5. [String Matching (KMP Basics)](#5-string-matching-kmp-basics)
6. [String Building Patterns](#6-string-building-patterns)

---

## 1. Sliding Window on Strings

### 📖 What is it?
A "window" that slides across the string, keeping track of characters inside it. Perfect for substring problems!

### 🤔 The Problem It Solves
"Find the longest/shortest substring that satisfies some condition"

### 💡 The Intuition

Imagine a magnifying glass sliding across text:

```
String: "abcabcbb"
Window: [   ]  → slides right

Step 1: [a]bcabcbb     → unique chars: {a}
Step 2: [ab]cabcbb     → unique chars: {a,b}
Step 3: [abc]abcbb     → unique chars: {a,b,c}
Step 4: [abca]bcbb     → 'a' repeats! Shrink from left
Step 5: a[bca]bcbb     → now unique again
...
```

### 🔑 When To Use It
- **Keywords:** "longest substring", "shortest substring", "window", "consecutive characters"
- **You're looking for:** A contiguous part of the string with some property

### 💻 The Code (Longest Substring Without Repeating)

```python
def length_of_longest_substring(s: str) -> int:
    seen = {}  # char -> last index where we saw it
    left = 0
    max_len = 0
    
    for right, char in enumerate(s):
        # If we've seen this char in our current window
        if char in seen and seen[char] >= left:
            # Move left pointer past the duplicate
            left = seen[char] + 1
        
        seen[char] = right
        max_len = max(max_len, right - left + 1)
    
    return max_len
```

### 📺 Learn More
- [NeetCode - Longest Substring Without Repeating](https://www.youtube.com/watch?v=wiGpQwVHdE0)

---

## 2. Two Pointers for Strings

### 📖 What is it?
Using two index variables to traverse the string, either from both ends (opposite direction) or same direction.

### 🤔 The Problem It Solves
Palindrome checking, string reversal, comparing from both ends.

### 💡 The Intuition

**Opposite Direction (Palindrome Check):**
```
String: "racecar"
         ↑     ↑
        left  right

Compare: r == r ✓
Move inward: a == a ✓
Continue: c == c ✓
Middle: e
It's a palindrome! ✅
```

**Same Direction (Remove Duplicates):**
```
String: "aabbcc"
         ↑
        slow
         ↑
        fast

Keep slow at "write position", fast scans ahead.
```

### 🔑 When To Use It
- **Keywords:** "palindrome", "reverse", "in-place", "compare from ends"
- **You want:** O(1) extra space

### 💻 The Code

```python
# Palindrome check
def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Reverse string (in-place, for char array)
def reverse_string(s: list) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
```

### 📺 Learn More
- [NeetCode - Valid Palindrome](https://www.youtube.com/watch?v=jJXJ16kPFWg)

---

## 3. Anagram Detection

### 📖 What is it?
Checking if two strings have the exact same characters, just in different order.

### 🤔 The Problem It Solves
"Is 'listen' an anagram of 'silent'?" → Yes!

### 💡 The Intuition

Think of it like **counting letters**:

```
"listen" → {l:1, i:1, s:1, t:1, e:1, n:1}
"silent" → {s:1, i:1, l:1, e:1, n:1, t:1}

Same counts? → Anagram! ✅
```

Alternative: **Sort both strings**
```
"listen" → "eilnst"
"silent" → "eilnst"

Same sorted? → Anagram! ✅
```

### 🔑 When To Use It
- **Keywords:** "anagram", "permutation", "same characters"
- **Variations:** Find all anagrams, group anagrams

### 💻 The Code

```python
from collections import Counter

# Simple anagram check - O(n)
def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

# Using sorting - O(n log n)
def is_anagram_sort(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

# Group anagrams together
def group_anagrams(strs: list) -> list:
    groups = {}
    for s in strs:
        # Use sorted string as key
        key = tuple(sorted(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values())
```

### 📺 Learn More
- [NeetCode - Valid Anagram](https://www.youtube.com/watch?v=9UtInBqnCgA)
- [NeetCode - Group Anagrams](https://www.youtube.com/watch?v=vzdNOK2oB2E)

---

## 4. Palindrome Patterns

### 📖 What is it?
A string that reads the same forwards and backwards.

### 🤔 Problems It Solves
- Check if palindrome
- Find longest palindromic substring
- Make string a palindrome with minimum changes

### 💡 The Intuition

**Expand from Center:**
```
For each position, try to expand outward:

String: "babad"

At 'a' (index 1):
   ← a →
   b a b   ✓ palindrome "bab"!
   
At 'b' (index 2):
   ← b →
   a b a   ✓ palindrome "aba"!
```

Key insight: A palindrome can have:
- **Odd length:** One center character (expand from 1 char)
- **Even length:** Two center characters (expand from 2 chars)

### 💻 The Code

```python
def longest_palindrome(s: str) -> str:
    def expand(left: int, right: int) -> str:
        # Expand while characters match
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the palindrome (note: left and right are now outside)
        return s[left + 1:right]
    
    result = ""
    for i in range(len(s)):
        # Odd length palindrome (single center)
        odd = expand(i, i)
        if len(odd) > len(result):
            result = odd
        
        # Even length palindrome (two centers)
        even = expand(i, i + 1)
        if len(even) > len(result):
            result = even
    
    return result
```

### 💡 Can We Form a Palindrome?

A string can be rearranged into a palindrome if:
- At most ONE character has an odd frequency

```python
def can_form_palindrome(s: str) -> bool:
    from collections import Counter
    freq = Counter(s)
    odd_count = sum(1 for v in freq.values() if v % 2 == 1)
    return odd_count <= 1
```

### 📺 Learn More
- [NeetCode - Longest Palindromic Substring](https://www.youtube.com/watch?v=XYQecbcd6_c)
- [NeetCode - Palindromic Substrings](https://www.youtube.com/watch?v=4RACzI5-du8)

---

## 5. String Matching (KMP Basics)

### 📖 What is it?
Finding where a pattern appears in a text. KMP (Knuth-Morris-Pratt) does it in O(n+m) instead of O(n*m).

### 🤔 The Problem It Solves
"Find all occurrences of 'abc' in 'ababcabc'"

### 💡 The Intuition (Simple Version First)

**Naive approach (what you'd naturally do):**
```
Text:    "ababcabc"
Pattern: "abc"

Try at position 0: aba... → 'a' matches, 'b' matches, 'a'≠'c' ✗
Try at position 1: bab... → 'b'≠'a' ✗
Try at position 2: abc... → all match! ✓ Found at 2
...
```

**Why KMP is smarter:**
When a mismatch happens, KMP doesn't start over. It uses pre-computed information about the pattern to skip ahead.

### 💻 Simple Version (Good Enough for Most Interviews)

```python
# Python's built-in is usually fine!
def find_pattern(text: str, pattern: str) -> int:
    return text.find(pattern)  # Returns -1 if not found

# Find all occurrences
def find_all(text: str, pattern: str) -> list:
    result = []
    start = 0
    while True:
        idx = text.find(pattern, start)
        if idx == -1:
            break
        result.append(idx)
        start = idx + 1
    return result
```

### 💻 KMP (If Asked in Interview)

```python
def kmp_search(text: str, pattern: str) -> int:
    if not pattern:
        return 0
    
    # Build failure function (LPS array)
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1
    
    # Search
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                return i - j  # Found!
        elif j > 0:
            j = lps[j - 1]
        else:
            i += 1
    
    return -1
```

> 💡 **Interview Tip:** For most interviews, using Python's `find()` or `in` is acceptable. Only implement KMP if specifically asked!

---

## 6. String Building Patterns

### 📖 What is it?
Efficiently constructing new strings from pieces.

### 🤔 The Problem It Solves
Build a result string without O(n²) performance.

### 💡 The Intuition

**Why Concatenation is Slow:**
```python
# Each += creates a NEW string!
s = ""
s += "a"    # Creates "a" (1 char copied)
s += "b"    # Creates "ab" (2 chars copied)
s += "c"    # Creates "abc" (3 chars copied)
# Total: 1+2+3+...+n = O(n²) operations!
```

**Solution: Use a List**
```python
# Appending to list is O(1)
parts = []
parts.append("a")
parts.append("b")
parts.append("c")
s = "".join(parts)  # One O(n) operation at the end
```

### 💻 Pattern Template

```python
def build_string_efficiently(chars):
    result = []
    for c in chars:
        # Do some processing
        if some_condition(c):
            result.append(c.upper())
        else:
            result.append(c)
    return "".join(result)
```

### Common String Building Scenarios

```python
# Remove certain characters
def remove_vowels(s):
    vowels = set('aeiouAEIOU')
    return ''.join(c for c in s if c not in vowels)

# Transform characters
def encode(s):
    result = []
    for c in s:
        result.append(chr(ord(c) + 1))  # Shift by 1
    return ''.join(result)

# Conditional building
def compress(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(s[i-1] + str(count))
            count = 1
    result.append(s[-1] + str(count))
    return ''.join(result)
```

---

## 🎯 Quick Decision Guide

| Problem Type | Pattern |
|-------------|---------|
| "Is palindrome?" | Two Pointers (both ends) |
| "Longest palindrome substring" | Expand from center |
| "Anagram check" | Counter/HashMap |
| "Group anagrams" | Sort as key + HashMap |
| "Longest substring with property" | Sliding Window |
| "Find pattern in text" | Built-in find() or KMP |
| "Build result string" | List + Join |
| "Reverse string" | Two Pointers |
| "Valid parentheses" | Stack |

---

> 💡 **Pro tip:** In interviews, always clarify: "Should I consider case sensitivity?" "What about spaces and special characters?"
