# 🎯 DSA Master Cheatsheet - Python

> **Your one-stop quick reference for coding interviews!**

---

## 📊 Pattern Recognition Guide

| Keywords | Pattern | Data Structure |
|----------|---------|----------------|
| "sorted array" | Binary Search / Two Pointers | Array |
| "pair with sum" | Two Pointers / HashMap | Array/Hash |
| "subarray" | Sliding Window / Prefix Sum | Array |
| "k elements" | Heap | Heap |
| "shortest path (unweighted)" | BFS | Queue |
| "shortest path (weighted)" | Dijkstra | Heap |
| "connected components" | DFS / Union-Find | Graph |
| "dependencies/ordering" | Topological Sort | Graph |
| "all combinations" | Backtracking | Recursion |
| "optimal substructure" | DP | Array/HashMap |
| "prefix matching" | Trie | Trie |
| "overlapping intervals" | Sort + Merge | Array |
| "next greater" | Monotonic Stack | Stack |
| "balanced brackets" | Stack | Stack |
| "level by level" | BFS | Queue |

---

## ⚡ Big-O Quick Reference

### Time Complexity

| Algorithm | Best | Average | Worst |
|-----------|------|---------|-------|
| Binary Search | O(1) | O(log n) | O(log n) |
| Array Access | O(1) | O(1) | O(1) |
| HashMap Get/Set | O(1) | O(1) | O(n) |
| BST Search | O(log n) | O(log n) | O(n) |
| Heap Push/Pop | O(log n) | O(log n) | O(log n) |
| QuickSort | O(n log n) | O(n log n) | O(n²) |
| MergeSort | O(n log n) | O(n log n) | O(n log n) |
| BFS/DFS | O(V + E) | O(V + E) | O(V + E) |

### Space Complexity

| Data Structure | Space |
|----------------|-------|
| Array | O(n) |
| HashMap | O(n) |
| Recursion | O(depth) |
| BFS | O(width) |
| DFS | O(height) |

---

## 🐍 Python Quick Reference

```python
# Collections
from collections import deque, Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right

# Counter
freq = Counter(nums)
freq.most_common(k)

# defaultdict
graph = defaultdict(list)
d = defaultdict(int)

# Heap (min-heap)
heappush(heap, val)
heappop(heap)
# Max-heap: use negative values

# Deque
q = deque()
q.append(x)      # Right
q.appendleft(x)  # Left
q.popleft()      # Front
q.pop()          # Back

# Sorting
arr.sort()                     # In-place
sorted(arr)                    # Returns new
arr.sort(key=lambda x: x[1])   # By key
arr.sort(reverse=True)         # Descending
```

---

## 🔥 Must-Know Templates

### Binary Search
```python
def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target: return m
        elif arr[m] < target: l = m + 1
        else: r = m - 1
    return -1
```

### Two Pointers
```python
l, r = 0, len(arr) - 1
while l < r:
    if condition: l += 1
    else: r -= 1
```

### Sliding Window
```python
l = 0
for r in range(len(arr)):
    # Add arr[r] to window
    while invalid:
        # Remove arr[l] from window
        l += 1
    # Update result
```

### BFS
```python
queue = deque([start])
visited = {start}
while queue:
    node = queue.popleft()
    for nei in graph[node]:
        if nei not in visited:
            visited.add(nei)
            queue.append(nei)
```

### DFS
```python
def dfs(node, visited):
    visited.add(node)
    for nei in graph[node]:
        if nei not in visited:
            dfs(nei, visited)
```

### Backtracking
```python
def backtrack(path, choices):
    if is_solution(path):
        result.append(path[:])
        return
    for choice in choices:
        path.append(choice)
        backtrack(path, remaining)
        path.pop()
```

### DP Template
```python
# Top-down
def dp(state, memo={}):
    if base_case: return base_value
    if state in memo: return memo[state]
    memo[state] = recurrence
    return memo[state]

# Bottom-up
dp = [0] * (n + 1)
for i in range(n):
    dp[i] = transition
```

---

## 📚 Topic Index

| # | Topic | Key Concepts |
|---|-------|--------------|
| 01 | [Arrays](../01_Arrays/) | Two Pointers, Sliding Window, Prefix Sum |
| 02 | [Strings](../02_Strings/) | Anagrams, Palindromes, KMP |
| 03 | [Linked Lists](../03_Linked_Lists/) | Fast/Slow, Reversal, Merge |
| 04 | [Stacks](../04_Stacks/) | Monotonic Stack, Matching |
| 05 | [Queues](../05_Queues/) | BFS, Level Order |
| 06 | [Hash Tables](../06_Hash_Tables/) | Two Sum, Grouping |
| 07 | [Trees](../07_Trees/) | DFS, BFS, BST |
| 08 | [Heaps](../08_Heaps/) | Top-K, Two Heaps |
| 09 | [Graphs](../09_Graphs/) | BFS, DFS, Dijkstra, Topo Sort |
| 10 | [Recursion](../10_Recursion_Backtracking/) | Subsets, Permutations |
| 11 | [DP](../11_Dynamic_Programming/) | Knapsack, LCS, LIS |
| 12 | [Greedy](../12_Greedy/) | Intervals, Jump Game |
| 13 | [Bit Manipulation](../13_Bit_Manipulation/) | XOR, Bit Counting |
| 14 | [Tries](../14_Tries/) | Prefix Search |
| 15 | [Intervals](../15_Intervals/) | Merge, Insert |
| 16 | [Math](../16_Math_Geometry/) | Matrix, Primes |

---

## 🎯 Interview Prep Checklist

- [ ] Arrays: Two Sum, 3Sum, Sliding Window Max
- [ ] Strings: Valid Palindrome, Longest Substring
- [ ] Linked Lists: Reverse, Detect Cycle, Merge
- [ ] Trees: Traversals, LCA, Validate BST
- [ ] Graphs: BFS, DFS, Topo Sort
- [ ] DP: Climbing Stairs, Coin Change, LCS
- [ ] Heap: Top K, Merge K Sorted
- [ ] Backtracking: Subsets, Permutations

---

> 📌 **Print this and review before interviews!**
