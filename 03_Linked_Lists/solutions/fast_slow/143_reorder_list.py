from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Problem: 143. Reorder List
        Link: https://leetcode.com/problems/reorder-list/
        
        You are given the head of a singly linked-list. The list can be represented as:
        L0 → L1 → … → Ln - 1 → Ln
        Reorder the list to be on the following form:
        L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
        
        Do not return anything, modify head in-place instead.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not head or not head.next:
            return
            
        # 1. Find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 2. Reverse second half
        # Separating the two halves is good practice but strict reverse suffices
        curr = slow.next
        slow.next = None # Break the link
        
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        # prev is now head of second half
        
        # 3. Merge the two halves
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
