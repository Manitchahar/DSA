from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Problem: 206. Reverse Linked List
        Link: https://leetcode.com/problems/reverse-linked-list/
        
        Given the head of a singly linked list, reverse the list, and return the reversed list.
        
        Time Complexity: O(n) - We visit every node exactly once.
        Space Complexity: O(1) - Iterative approach uses constant extra space.
        """
        prev = None
        curr = head
        
        while curr:
            # 1. Save the next node so we don't lose the rest of the list
            next_temp = curr.next
            
            # 2. Reverse the pointer direction
            curr.next = prev
            
            # 3. Move pointers forward
            prev = curr
            curr = next_temp
            
        return prev

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Recursive approach.
        Space Complexity: O(n) due to recursion stack.
        """
        if not head or not head.next:
            return head
            
        new_head = self.reverseListRecursive(head.next)
        
        # Reverse the link between head and head.next
        head.next.next = head
        head.next = None
        
        return new_head
