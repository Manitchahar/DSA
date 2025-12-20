# 📚 Linked Lists - Complete DSA Guide (Python)

> **Master the art of pointer manipulation!**

---

## 🎯 What You'll Master

- Singly & Doubly Linked List fundamentals
- Time & Space complexity for all operations
- Essential patterns: Fast/Slow pointers, Reversal, Merge
- 25+ curated LeetCode problems
- Common pitfalls and debugging tips

---

## 📖 Table of Contents

1. [Fundamentals](#-fundamentals)
2. [Python Implementation](#-python-implementation)
3. [Core Operations & Complexity](#-core-operations--complexity)
4. [Essential Patterns](#-essential-patterns)
5. [Common Pitfalls](#-common-pitfalls)
6. [Mastery Checklist](#-mastery-checklist)

---

## 🔥 Fundamentals

### What is a Linked List?

A **linked list** is a linear data structure where elements are stored in **nodes**, and each node points to the next one.

```
Singly Linked List:
┌───────┐    ┌───────┐    ┌───────┐    ┌───────┐
│ 1 | ●─┼───►│ 2 | ●─┼───►│ 3 | ●─┼───►│ 4 | ⊥ │
└───────┘    └───────┘    └───────┘    └───────┘
  head                                    tail

Doubly Linked List:
         ┌───────────┐    ┌───────────┐    ┌───────────┐
         │ ⊥ | 1 | ●─┼───►│ ●─| 2 | ●─┼───►│ ●─| 3 | ⊥ │
         └───────────┘◄───┼───────────┘◄───┼───────────┘
           head                               tail
```

### Linked List vs Array

| Feature | Array | Linked List |
|---------|-------|-------------|
| Access by index | O(1) ✅ | O(n) ❌ |
| Insert at beginning | O(n) | O(1) ✅ |
| Insert at end | O(1)* | O(1) with tail ✅ |
| Insert in middle | O(n) | O(1) if at node ✅ |
| Delete | O(n) | O(1) if at node ✅ |
| Memory | Contiguous | Scattered |
| Extra space | None | Pointer per node |

### When to Use Linked Lists?

✅ **Use when:**
- Frequent insertions/deletions at beginning
- Don't need random access
- Dynamic size with many insertions
- Implementing stacks, queues, graphs

❌ **Don't use when:**
- Need frequent random access by index
- Memory is tight (pointers add overhead)
- Need cache-friendly performance

---

## 🐍 Python Implementation

### Node Classes

```python
# Singly Linked List Node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Doubly Linked List Node
class DListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
```

### Building a Linked List

```python
# From values
def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# Usage
head = build_list([1, 2, 3, 4, 5])
```

### Traversing a Linked List

```python
def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result
```

### Getting Length

```python
def get_length(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length
```

---

## ⚡ Core Operations & Complexity

### Time Complexity

| Operation | Singly | Doubly | Notes |
|-----------|--------|--------|-------|
| Access by index | O(n) | O(n) | Must traverse |
| Search | O(n) | O(n) | Linear scan |
| Insert at head | O(1) | O(1) | Update pointers |
| Insert at tail | O(n) or O(1)* | O(1) | *With tail pointer |
| Insert after node | O(1) | O(1) | Have the node |
| Delete head | O(1) | O(1) | |
| Delete tail | O(n) | O(1) | Doubly has prev |
| Delete node | O(1) | O(1) | If have the node |

### Space Complexity

Each node uses O(1) extra space for pointer(s).
Total: O(n) for n nodes.

---

## 🎨 Essential Patterns

### 1️⃣ Dummy Head (Sentinel Node)

**When to use:** When head might change or need simpler code.

```python
def remove_elements(head, val):
    """Remove all nodes with value = val"""
    dummy = ListNode(0)
    dummy.next = head
    
    curr = dummy
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next  # Skip the node
        else:
            curr = curr.next
    
    return dummy.next  # New head
```

### 2️⃣ Fast and Slow Pointers (Floyd's Algorithm)

**When to use:** Finding middle, detecting cycles, finding cycle start.

```python
# Find middle node
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow  # Middle (or first of two middles)

# Detect cycle
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Find cycle start (if cycle exists)
def find_cycle_start(head):
    slow = fast = head
    
    # Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # No cycle
    
    # Find start: move one pointer to head, both move at same speed
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow  # Cycle start
```

### 3️⃣ Reverse Linked List

**When to use:** Reverse entire list, reverse part of list, check palindrome.

```python
# Iterative reversal
def reverse_list(head):
    prev = None
    curr = head
    
    while curr:
        next_temp = curr.next  # Save next
        curr.next = prev       # Reverse pointer
        prev = curr            # Move prev forward
        curr = next_temp       # Move curr forward
    
    return prev  # New head

# Recursive reversal
def reverse_list_recursive(head):
    if not head or not head.next:
        return head
    
    new_head = reverse_list_recursive(head.next)
    head.next.next = head  # Reverse the link
    head.next = None       # Avoid cycle
    
    return new_head
```

### 4️⃣ Merge Two Sorted Lists

```python
def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    
    # Attach remaining
    curr.next = l1 or l2
    
    return dummy.next
```

### 5️⃣ Remove Nth Node From End

```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    
    # Move fast pointer n+1 steps ahead
    fast = dummy
    for _ in range(n + 1):
        fast = fast.next
    
    # Move both until fast reaches end
    slow = dummy
    while fast:
        slow = slow.next
        fast = fast.next
    
    # Remove the node
    slow.next = slow.next.next
    
    return dummy.next
```

### 6️⃣ Intersection of Two Lists

```python
def get_intersection_node(headA, headB):
    if not headA or not headB:
        return None
    
    pA, pB = headA, headB
    
    # When one reaches end, redirect to other list's head
    # They'll meet at intersection or both become None
    while pA != pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA
    
    return pA
```

### 7️⃣ Check Palindrome

```python
def is_palindrome(head):
    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    prev = None
    while slow:
        next_temp = slow.next
        slow.next = prev
        prev = slow
        slow = next_temp
    
    # Compare
    left, right = head, prev
    while right:  # Right is shorter or equal
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    
    return True
```

---

## 🧠 Problem-Solving Framework

### Pattern Recognition

| Keyword | Pattern |
|---------|---------|
| "middle of list" | Fast/Slow pointers |
| "cycle detection" | Fast/Slow (Floyd's) |
| "reverse" | Three-pointer reversal |
| "merge sorted lists" | Dummy head + comparison |
| "nth from end" | Two pointers, n apart |
| "palindrome" | Reverse second half |
| "intersection" | Length difference or two-pointer trick |
| "reorder list" | Find middle + reverse + merge |

---

## ⚠️ Common Pitfalls

### 1. Losing Head Reference

```python
# ❌ Wrong - lost the head!
while head:
    head = head.next  # Can't return original head

# ✅ Correct - use a separate pointer
curr = head
while curr:
    curr = curr.next
return head  # Still have original head
```

### 2. NullPointerException (None.next)

```python
# ❌ Crashes if fast is None
while fast.next:  # Error if fast is None!

# ✅ Check fast first
while fast and fast.next:
```

### 3. Forgetting to Update Links

```python
# When inserting node B between A and C:
# ❌ Wrong order - loses C
A.next = B
B.next = C  # But we lost C!

# ✅ Correct - save or reverse order
B.next = A.next  # First point B to C
A.next = B       # Then point A to B
```

### 4. Creating Cycles Accidentally

```python
# When reversing, forgetting to set tail.next = None
def reverse(head):
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    # head now points to second node - creates cycle if not handled!
    return prev
```

### 5. Edge Cases

Always consider:
- Empty list (`head = None`)
- Single node list
- Two node list
- Cycle in list (if applicable)

---

## 🧪 Required Drills

You should be able to code each in **≤ 10 minutes**:

- [ ] Implement ListNode class
- [ ] Build linked list from array
- [ ] Traverse and print linked list
- [ ] Find length of linked list
- [ ] Reverse linked list (iterative)
- [ ] Reverse linked list (recursive)
- [ ] Find middle node
- [ ] Detect cycle
- [ ] Merge two sorted lists
- [ ] Remove nth node from end
- [ ] Check if palindrome

---

## 🏁 Mastery Checklist

- [ ] I can draw pointer movements for reversal without code
- [ ] I know when to use dummy head
- [ ] I can explain why fast/slow pointers find middle
- [ ] I can detect and find cycle start
- [ ] I handle edge cases: empty, single node, two nodes
- [ ] I know time/space complexity for all operations

---

## 📁 Directory Structure

```
03_Linked_Lists/
├── README.md              # This file
├── cheatsheet.md          # Quick reference
├── algorithms_explained.md # Deep dives
├── leetcode_problems.md   # Curated problems
└── solutions/             # Your practice code
    ├── reversal/
    ├── fast_slow/
    ├── merge/
    └── two_pointers/
```

---

## 🚀 Next Steps

1. Read the [Cheat Sheet](./cheatsheet.md)
2. Study [Algorithms Explained](./algorithms_explained.md)
3. Practice [LeetCode Problems](./leetcode_problems.md)

---

> 💡 **Pro Tip:** Always draw the linked list and trace pointers on paper first!

Happy Coding! 🎯
