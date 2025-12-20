from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Problem: 142. Linked List Cycle II
        Link: https://leetcode.com/problems/linked-list-cycle-ii/
        
        Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
        
        Time Complexity: O(n) - Two passes max.
        Space Complexity: O(1)
        """
        slow, fast = head, head
        
        # 1. Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None # No cycle found
        
        # 2. Find entry point
        # Distance from head to cycle_start = Distance from meeting_point to cycle_start (in specific frame)
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        return slow
