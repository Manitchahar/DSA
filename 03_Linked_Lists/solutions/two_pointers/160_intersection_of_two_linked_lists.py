from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        Problem: 160. Intersection of Two Linked Lists
        Link: https://leetcode.com/problems/intersection-of-two-linked-lists/
        
        Given the heads of two singly linked lists headA and headB, return the node at which the two lists intersect.
        If the two linked lists have no intersection at all, return null.
        
        Time Complexity: O(n + m)
        Space Complexity: O(1)
        """
        if not headA or not headB:
            return None
        
        ptrA = headA
        ptrB = headB
        
        # Logic: If they have different lengths, switching heads equalizes the distance traveled.
        # A + B = B + A
        # If they intersect, they will meet at the intersection node.
        # If they don't, they will both hit None (end) at the same time.
        
        while ptrA != ptrB:
            ptrA = ptrA.next if ptrA else headB
            ptrB = ptrB.next if ptrB else headA
            
        return ptrA
