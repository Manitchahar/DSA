from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Problem: 876. Middle of the Linked List
        Link: https://leetcode.com/problems/middle-of-the-linked-list/
        
        Given the head of a singly linked list, return the middle node of the linked list.
        If there are two middle nodes, return the second middle node.
        
        Time Complexity: O(n) - One pass.
        Space Complexity: O(1)
        """
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
