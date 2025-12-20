# 🧠 Tries (Prefix Trees) Explained (For Beginners!)

> **No jargon. Just plain English explanations.**

---

## Table of Contents
1. [The "Trie" Mental Model](#1-the-trie-mental-model)
2. [Building the Structure](#2-building-the-structure)
3. [The "Wildcard" Search](#3-the-wildcard-search-add-and-search)
4. [Trie + Backtracking (Word Search II)](#4-trie--backtracking-word-search-ii)

---

## 1. The "Trie" Mental Model

### 📖 What is it?
A specific type of tree used for storing **Strings**.
It saves space by sharing common prefixes.

### 🤔 The Real World Analogy
*   **Auto-complete:** You type "ap", and it suggests "apple", "app", "application". They all share the "ap" path.
*   **Dictionary:** Organizing words by starting letter.

### 💡 The Visual
Words: `["apple", "app", "ape"]`

```
        (root)
           |
          [a]
           |
          [p]  <-- Ended? False (Waiting for 'p' or 'e')
         /   \
       [p]   [e]  <-- Ended? True ("ape")
        |
       [l]
        |
       [e]  <-- Ended? True ("apple")
```
Note: "app" also ends at the second `[p]`. We mark nodes as `isEndOfWord`.

---

## 2. Building the Structure

### 💻 The Node
Instead of `left` and `right`, we have `children`.
`children` is usually a HashMap: `char -> TrieNode`.

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
```

### 💻 Insertion (Loop)
1.  Start at root.
2.  For each char in word:
    *   If char not in children, create new node.
    *   Move to child.
3.  Mark last node as `endOfWord = True`.

```python
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
```

### 💻 Search (Loop)
Same as insert, but return `False` if char is missing.

```python
    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord
        
    def startsWith(self, prefix):
        # Same as search, but don't check endOfWord
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
```

### 📺 Learn More
- [NeetCode - Implement Trie](https://www.youtube.com/watch?v=oobqoCJlHA0)

---

## 3. The "Wildcard" Search (Add and Search)

### 📖 What is it?
Searching with `.` where `.` matches ANY character.
`search("b.d")` matches `"bad"`, `"bed"`.

### 💡 The Logic
Since `.` can be anything, we must try **ALL** children at that level. This requires **DFS (Recursion)** instead of a simple loop.

### 💻 The Code

```python
def search(self, word):
    def dfs(j, root):
        cur = root
        
        for i in range(j, len(word)):
            c = word[i]
            if c == ".":
                # Backtracking: Try all children
                for child in cur.children.values():
                    if dfs(i + 1, child):
                        return True
                return False
            else:
                if c not in cur.children:
                    return False
                cur = cur.children[c]
                
        return cur.endOfWord
        
    return dfs(0, self.root)
```

### 📺 Learn More
- [NeetCode - Design Add and Search](https://www.youtube.com/watch?v=BTf05gs_8iU)

---

## 4. Trie + Backtracking (Word Search II)

### 📖 What is it?
Finding ALL words from a dictionary that exist in a 2D Boggle board.

### 🤔 The Problem with Naive Approach
Iterating every word in dictionary and running DFS on board is too slow.
`O(Words * BoardSize)`

### 💡 The Optimization
Turn the **Dictionary** into a **Trie**.
Run DFS **ONCE** on the board. As you move on the board, move down the Trie.
*   If prefix `ab` doesn't exist in Trie, stop exploring that path on board immediately!
*   **Pruning:** Remove words from Trie once found to avoid duplicate checks.

### 📺 Learn More
- [NeetCode - Word Search II](https://www.youtube.com/watch?v=asbcE9mZz_U)

---

## 🎯 Quick Decision Guide

| Problem Type | Pattern |
|-------------|---------|
| "Prefix search", "Autocomplete" | **Basic Trie** |
| "Wildcard (.)" | **Trie + DFS** |
| "Word Search with Dictionary" | **Trie + Grid DFS** |
| "XOR of max two numbers" | **Binary Trie** (0/1 branches) |

---
