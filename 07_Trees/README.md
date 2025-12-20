# 📚 Trees - Complete DSA Guide (Python)

> **Master hierarchical data structures!**

---

## 🎯 What You'll Master

- Binary Trees, BST, and their properties
- Tree traversals (DFS and BFS)
- Essential patterns: Recursion, Path problems, Construction
- 30+ curated LeetCode problems

---

## 🔥 Fundamentals

### What is a Tree?

A **tree** is a hierarchical data structure with nodes connected by edges. Each node has exactly one parent (except the root).

```
        1           ← Root
       / \
      2   3         ← Level 1
     / \   \
    4   5   6       ← Level 2 (Leaves: 4, 5, 6)
```

### Key Terms

| Term | Definition |
|------|------------|
| **Root** | Top node (no parent) |
| **Leaf** | Node with no children |
| **Height** | Longest path from root to leaf |
| **Depth** | Distance from root to node |
| **Subtree** | Tree formed by a node and its descendants |

### Binary Tree vs BST

| Binary Tree | BST (Binary Search Tree) |
|-------------|-------------------------|
| Each node has ≤2 children | Left < Parent < Right |
| No ordering required | Ordered for fast search |
| O(n) search | O(log n) search (balanced) |

---

## 🐍 Python Implementation

### Node Class

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### Build Tree from List

```python
def build_tree(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root
```

---

## 🎨 Essential Patterns

### 1️⃣ DFS Traversals (Preorder, Inorder, Postorder)

```python
# Preorder: Root → Left → Right
def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

# Inorder: Left → Root → Right (sorted for BST!)
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

# Postorder: Left → Right → Root
def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]
```

### 2️⃣ BFS / Level Order Traversal

```python
from collections import deque

def level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    
    return result
```

### 3️⃣ Tree Height / Max Depth

```python
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

### 4️⃣ Same Tree / Symmetric Tree

```python
def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return (p.val == q.val and 
            is_same_tree(p.left, q.left) and 
            is_same_tree(p.right, q.right))

def is_symmetric(root):
    def is_mirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val and 
                is_mirror(t1.left, t2.right) and 
                is_mirror(t1.right, t2.left))
    return is_mirror(root, root)
```

### 5️⃣ Path Sum

```python
def has_path_sum(root, target):
    if not root:
        return False
    if not root.left and not root.right:  # Leaf
        return root.val == target
    return (has_path_sum(root.left, target - root.val) or
            has_path_sum(root.right, target - root.val))
```

### 6️⃣ Lowest Common Ancestor (LCA)

```python
def lca(root, p, q):
    if not root or root == p or root == q:
        return root
    
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    
    if left and right:
        return root
    return left or right
```

### 7️⃣ Validate BST

```python
def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    if root.val <= min_val or root.val >= max_val:
        return False
    return (is_valid_bst(root.left, min_val, root.val) and
            is_valid_bst(root.right, root.val, max_val))
```

### 8️⃣ Invert Binary Tree

```python
def invert_tree(root):
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root
```

### 9️⃣ Serialize / Deserialize

```python
def serialize(root):
    if not root:
        return "null"
    return f"{root.val},{serialize(root.left)},{serialize(root.right)}"

def deserialize(data):
    def build(nodes):
        val = next(nodes)
        if val == "null":
            return None
        node = TreeNode(int(val))
        node.left = build(nodes)
        node.right = build(nodes)
        return node
    return build(iter(data.split(",")))
```

---

## 🧠 Pattern Recognition

| Keyword | Pattern |
|---------|---------|
| "height/depth" | Recursion, return max |
| "path sum" | DFS with remaining sum |
| "level by level" | BFS |
| "validate BST" | Pass min/max bounds |
| "LCA" | Recursive search |
| "serialize" | Preorder with null markers |
| "invert/mirror" | Swap left and right |

---

## ⚠️ Common Pitfalls

```python
# 1) Forgetting base case
if not root:
    return ...

# 2) BST validation - need bounds, not just left < root < right
# Wrong: if root.left.val < root.val  (doesn't check all ancestors)
# Right: pass min/max bounds down

# 3) Modifying tree during traversal without intention
```

---

## 📁 Directory Structure

```
07_Trees/
├── README.md
├── cheatsheet.md
├── algorithms_explained.md
├── leetcode_problems.md
└── solutions/
    ├── traversal/
    ├── bst/
    └── construction/
```

---

> 💡 **Pro Tip:** Most tree problems use recursion. Think "What do I need from left subtree, right subtree, and current node?"

Happy Coding! 🎯
