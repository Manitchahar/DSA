from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Problem: 215. Kth Largest Element in an Array
        Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
        
        Given an integer array nums and an integer k, return the kth largest element in the array.
        
        Time Complexity: O(n log k)
        Space Complexity: O(k)
        """
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)
                
        return heap[0]
