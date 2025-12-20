from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Problem: 92. Reverse Linked List II
        Link: https://leetcode.com/problems/reverse-linked-list-ii/
        
        Reverse the nodes of the list from position left to position right.
        
        Time Complexity: O(n) - One pass.
        Space Complexity: O(1)
        """
        if not head or left == right:
            return head
        
        # Use a dummy node to handle edge case where left = 1 (head changes)
        dummy = ListNode(0, head)
        prev = dummy
        
        # 1. Reach node at position "left - 1"
        for _ in range(left - 1):
            prev = prev.next
        
        # prev is now just before the sub-list to reverse
        curr = prev.next
        
        # 2. Reverse the sub-list
        # The idea: Repeatedly move the 'next' node to the front of the sub-list
        # Example: 1 -> [2 -> 3 -> 4] -> 5, left=2, right=4
        # curr is 2.
        # Iteration 1: Move 3 to front: 1 -> 3 -> 2 -> 4 -> 5
        # Iteration 2: Move 4 to front: 1 -> 4 -> 3 -> 2 -> 5
        
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
            
        return dummy.next
