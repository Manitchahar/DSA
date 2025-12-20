from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        Problem: 86. Partition List
        Link: https://leetcode.com/problems/partition-list/
        
        Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
        You should preserve the original relative order of the nodes in each of the two partitions.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Create two separate lists: one for < x, one for >= x
        left_dummy = ListNode(0)
        right_dummy = ListNode(0)
        left = left_dummy
        right = right_dummy
        
        curr = head
        while curr:
            if curr.val < x:
                left.next = curr
                left = left.next
            else:
                right.next = curr
                right = right.next
            curr = curr.next
            
        # Join them
        right.next = None    # Important! Avoid cycle.
        left.next = right_dummy.next
        
        return left_dummy.next
