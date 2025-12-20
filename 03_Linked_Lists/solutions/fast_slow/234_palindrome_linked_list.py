from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Problem: 234. Palindrome Linked List
        Link: https://leetcode.com/problems/palindrome-linked-list/
        
        Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
        
        Time Complexity: O(n)
        Space Complexity: O(1) - Modifies list effectively then restores it (optional).
        """
        if not head or not head.next:
            return True
        
        # 1. Find the middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # slow is now at the middle (or start of second half)
        
        # 2. Reverse the second half
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # prev is now the head of reversed second half
        
        # 3. Compare first half and second half
        left, right = head, prev
        while right: # Only need to check right (it might be shorter or same length)
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True
