from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Problem: 61. Rotate List
        Link: https://leetcode.com/problems/rotate-list/
        
        Given the head of a linked list, rotate the list to the right by k places.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not head or not head.next or k == 0:
            return head
            
        # 1. Find length and tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
            
        # 2. Compute effective k
        k = k % length
        if k == 0:
            return head
            
        # 3. Create circle
        tail.next = head
        
        # 4. Find new tail (length - k - 1 steps)
        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
            
        # 5. Break circle and return new head
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
