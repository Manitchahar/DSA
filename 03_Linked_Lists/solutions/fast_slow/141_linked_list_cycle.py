from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Problem: 141. Linked List Cycle
        Link: https://leetcode.com/problems/linked-list-cycle/
        
        Given head, the head of a linked list, determine if the linked list has a cycle in it.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Floyd's Cycle-Finding Algorithm
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next          # 1 step
            fast = fast.next.next     # 2 steps
            
            if slow == fast:
                return True           # Collision implies cycle
        
        return False
