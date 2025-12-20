# 🚀 Trees Cheat Sheet - Python

> Quick reference for tree problems

---

## ⚡ Node Definition

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

---

## 🎯 Traversal Templates

### DFS - Recursive

```python
# Preorder: Root → Left → Right
def preorder(root):
    if not root: return []
    return [root.val] + preorder(root.left) + preorder(root.right)

# Inorder: Left → Root → Right (BST = sorted!)
def inorder(root):
    if not root: return []
    return inorder(root.left) + [root.val] + inorder(root.right)

# Postorder: Left → Right → Root
def postorder(root):
    if not root: return []
    return postorder(root.left) + postorder(root.right) + [root.val]
```

### DFS - Iterative

```python
def inorder_iterative(root):
    res, stack = [], []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        res.append(root.val)
        root = root.right
    return res
```

### BFS - Level Order

```python
from collections import deque

def level_order(root):
    if not root: return []
    res, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        res.append(level)
    return res
```

---

## 🎯 Common Patterns

### Max Depth
```python
def max_depth(root):
    if not root: return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

### Same Tree
```python
def is_same(p, q):
    if not p and not q: return True
    if not p or not q: return False
    return p.val == q.val and is_same(p.left, q.left) and is_same(p.right, q.right)
```

### Invert Tree
```python
def invert(root):
    if not root: return None
    root.left, root.right = invert(root.right), invert(root.left)
    return root
```

### Path Sum
```python
def has_path_sum(root, target):
    if not root: return False
    if not root.left and not root.right:
        return root.val == target
    return has_path_sum(root.left, target - root.val) or \
           has_path_sum(root.right, target - root.val)
```

### LCA (Lowest Common Ancestor)
```python
def lca(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left and right: return root
    return left or right
```

### Validate BST
```python
def is_valid_bst(root, lo=float('-inf'), hi=float('inf')):
    if not root: return True
    if root.val <= lo or root.val >= hi: return False
    return is_valid_bst(root.left, lo, root.val) and \
           is_valid_bst(root.right, root.val, hi)
```

### Diameter
```python
def diameter(root):
    self.ans = 0
    def depth(node):
        if not node: return 0
        L, R = depth(node.left), depth(node.right)
        self.ans = max(self.ans, L + R)
        return 1 + max(L, R)
    depth(root)
    return self.ans
```

---

## 📊 Complexity

| Operation | Time |
|-----------|------|
| Traversal | O(n) |
| Height | O(n) |
| BST Search | O(h) - O(log n) balanced |
| BST Insert | O(h) |

---

## 🏷️ Pattern Recognition

| Keyword | Pattern |
|---------|---------|
| "depth/height" | Recursive max |
| "level by level" | BFS |
| "path sum" | DFS + subtract |
| "validate BST" | Pass bounds |
| "LCA" | Recursive search |
| "serialize" | Preorder + nulls |

---

> 📌 Remember: Most tree problems = recursion!
