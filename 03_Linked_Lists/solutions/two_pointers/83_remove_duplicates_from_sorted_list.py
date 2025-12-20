from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Problem: 83. Remove Duplicates from Sorted List
        Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
        
        Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        curr = head
        
        while curr and curr.next:
            if curr.val == curr.next.val:
                # Bypass the duplicate
                curr.next = curr.next.next
            else:
                # Move to next distinct element
                curr = curr.next
                
        return head
