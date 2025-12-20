from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Problem: 19. Remove Nth Node From End of List
        Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
        
        Given the head of a linked list, remove the nth node from the end of the list and return its head.
        
        Time Complexity: O(n) - One pass.
        Space Complexity: O(1)
        """
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # 1. Advance right pointer so there is a gap of n between left and right
        while n > 0 and right:
            right = right.next
            n -= 1
            
        # 2. Move both pointers until right reaches the end
        while right:
            left = left.next
            right = right.next
            
        # left is now at the node BEFORE the one we want to delete
        left.next = left.next.next
        
        return dummy.next
