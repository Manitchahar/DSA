from typing import Optional, List
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    # Necessary for heap comparison if values are equal
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Problem: 23. Merge k Sorted Lists
        Link: https://leetcode.com/problems/merge-k-sorted-lists/
        
        You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
        Merge all the linked-lists into one sorted linked-list and return it.
        
        Time Complexity: O(N log k) where N is the total number of nodes and k is the number of lists.
                         The heap operation takes O(log k) and we do it for every node.
        Space Complexity: O(k) for the heap.
        """
        min_heap = []
        
        # 1. Push the head of each list into the heap
        for l in lists:
            if l:
                heapq.heappush(min_heap, l)
        
        dummy = ListNode(0)
        curr = dummy
        
        # 2. Extract min and push next node
        while min_heap:
            node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next
            
            if node.next:
                heapq.heappush(min_heap, node.next)
                
        return dummy.next
