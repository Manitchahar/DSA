from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Problem: 25. Reverse Nodes in k-Group
        Link: https://leetcode.com/problems/reverse-nodes-in-k-group/
        
        Reverse the nodes of a linked list k at a time and return its modified list.
        If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as is.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            
            groupNext = kth.next
            
            # Reverse the group
            # We need to reverse between groupPrev and groupNext
            prev, curr = kth.next, groupPrev.next
            
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # Connect the reversed group back to the main list
            # groupPrev.next (start of group) now becomes the end, so it should point to groupNext
            # (already handled in reverse logic start 'prev = kth.next')
            
            # Update pointers for next iteration
            # Currently: groupPrev -> (start of reversed group) ... (end of reversed group) -> groupNext
            # We need to move groupPrev to the end of the reversed group
            
            tmp = groupPrev.next # This was the start, now it's the end
            groupPrev.next = kth # 'kth' was the end, now it's the start (prev variable held this)
            groupPrev = tmp
            
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
