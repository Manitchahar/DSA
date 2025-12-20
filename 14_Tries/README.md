# 📚 Tries (Prefix Trees) - DSA Guide

> **Efficient prefix-based string storage!**

---

## 🔥 What is a Trie?

A tree-like data structure for storing strings where each node represents a character.

```
Words: ["app", "apple", "api"]

         (root)
           |
           a
           |
           p
          / \
         p   i
        /     \
    [le]     [end]
```

---

## 🐍 Implementation

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True
    
    def search(self, word):
        node = self._find(word)
        return node is not None and node.is_end
    
    def startsWith(self, prefix):
        return self._find(prefix) is not None
    
    def _find(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return None
            node = node.children[c]
        return node
```

---

## 🎯 LeetCode Problems

| # | Problem | 📺 Video |
|---|---------|----------|
| 208 | [Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/) | [NeetCode](https://youtu.be/oobqoCJlHA0) |
| 211 | [Design Add and Search Words](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | [NeetCode](https://youtu.be/BTf05gs_8iU) |
| 212 | [Word Search II](https://leetcode.com/problems/word-search-ii/) | [NeetCode](https://youtu.be/asbcE9mZz_U) |

---

> 💡 Use trie when dealing with prefix queries on strings!
