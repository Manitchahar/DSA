# 🚀 Linked Lists Cheat Sheet - Python

> Quick reference for interviews and problem-solving

---

## ⚡ Node Definition

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

---

## 🧰 Basic Operations

```python
# ═══════════════════════════════════════════════════════
# BUILD FROM ARRAY
# ═══════════════════════════════════════════════════════
def build_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# ═══════════════════════════════════════════════════════
# CONVERT TO ARRAY
# ═══════════════════════════════════════════════════════
def to_array(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr

# ═══════════════════════════════════════════════════════
# GET LENGTH
# ═══════════════════════════════════════════════════════
def get_length(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count

# ═══════════════════════════════════════════════════════
# GET NTH NODE (0-indexed)
# ═══════════════════════════════════════════════════════
def get_nth(head, n):
    for _ in range(n):
        if not head:
            return None
        head = head.next
    return head
```

---

## 🎯 Pattern Templates

### Dummy Head (Sentinel)
```python
def some_operation(head):
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy
    
    # ... operations ...
    
    return dummy.next  # New head
```

### Fast/Slow - Find Middle
```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

### Fast/Slow - Detect Cycle
```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

### Fast/Slow - Find Cycle Start
```python
def find_cycle_start(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None
    
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow
```

### Reverse List (Iterative)
```python
def reverse(head):
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev
```

### Reverse List (Recursive)
```python
def reverse(head):
    if not head or not head.next:
        return head
    new_head = reverse(head.next)
    head.next.next = head
    head.next = None
    return new_head
```

### Merge Two Sorted Lists
```python
def merge(l1, l2):
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
    curr.next = l1 or l2
    return dummy.next
```

### Remove Nth From End
```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy
    
    for _ in range(n + 1):
        fast = fast.next
    
    while fast:
        slow = slow.next
        fast = fast.next
    
    slow.next = slow.next.next
    return dummy.next
```

### Intersection Point
```python
def get_intersection(headA, headB):
    pA, pB = headA, headB
    while pA != pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA
    return pA
```

### Check Palindrome
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
        tmp = slow.next
        slow.next = prev
        prev = slow
        slow = tmp
    
    # Compare
    while prev:
        if head.val != prev.val:
            return False
        head = head.next
        prev = prev.next
    return True
```

### Reorder List (L0→Ln→L1→Ln-1...)
```python
def reorder_list(head):
    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    prev = None
    curr = slow
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    
    # Merge alternating
    first, second = head, prev
    while second.next:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2
```

---

## 📊 Complexity Reference

| Operation | Singly | Doubly |
|-----------|--------|--------|
| Access by index | O(n) | O(n) |
| Insert at head | O(1) | O(1) |
| Insert at tail | O(n)* | O(1) |
| Insert after node | O(1) | O(1) |
| Delete head | O(1) | O(1) |
| Delete tail | O(n) | O(1) |
| Search | O(n) | O(n) |
| Find middle | O(n) | O(n) |
| Reverse | O(n) | O(n) |

*O(1) if maintaining tail pointer

---

## 💡 Pro Tips

### 1. Always Use Dummy Head When...
- Head might be deleted
- Need to return new head
- Simplifies edge cases

### 2. Draw Before Coding
```
Before: A -> B -> C
After:  C -> B -> A

Step 1: prev=None, curr=A
Step 2: prev=A, curr=B (A.next=None)
Step 3: prev=B, curr=C (B.next=A)
Step 4: prev=C, curr=None (C.next=B)
```

### 3. Common Pointer Update Pattern
```python
# Save before modifying
next_temp = curr.next
curr.next = something_else
curr = next_temp
```

### 4. Two Pointers Gap
```python
# To find nth from end, create gap of n
for _ in range(n):
    fast = fast.next

while fast:
    slow = slow.next
    fast = fast.next
# slow is now at nth from end
```

---

## ⚠️ Gotchas

```python
# 1) Check for None before accessing .next
while fast and fast.next:  # ✅ Check fast first!
    ...

# 2) Don't lose the head
curr = head  # ✅ Use separate pointer for traversal
while curr:
    curr = curr.next
return head  # Still have it

# 3) Update order matters
# To insert B after A:
B.next = A.next  # ✅ First!
A.next = B       # Then this

# 4) Handle single/empty lists
if not head or not head.next:
    return head
```

---

## 🏷️ Pattern Recognition

| Keyword | Pattern |
|---------|---------|
| "middle of list" | Fast/Slow pointers |
| "cycle" / "loop" | Floyd's algorithm |
| "reverse" | Three-pointer |
| "merge sorted" | Dummy + compare |
| "nth from end" | Two pointers, gap of n |
| "palindrome" | Reverse half + compare |
| "intersect" | Length diff or switch heads |
| "reorder" | Find middle + reverse + merge |
| "partition" | Two dummy heads |

---

> 📌 **Print this and keep it handy during practice!**
