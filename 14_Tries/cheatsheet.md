# 🚀 Tries Cheat Sheet

---

## ⚡ Trie Node & Operations

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

## When to Use

- Prefix matching
- Autocomplete
- Word search in dictionary
- IP routing

---

> 📌 Trie = efficient prefix-based string search
