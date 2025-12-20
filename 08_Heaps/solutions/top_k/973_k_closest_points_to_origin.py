from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Problem: 973. K Closest Points to Origin
        Link: https://leetcode.com/problems/k-closest-points-to-origin/
        
        Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
        
        Time Complexity: O(n log k)
        Space Complexity: O(k)
        """
        maxHeap = [] # Stores (-dist, x, y)
        
        for x, y in points:
            dist = -(x**2 + y**2) # Negate for max heap behavior
            heapq.heappush(maxHeap, (dist, x, y))
            
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
                
        return [[x, y] for (dist, x, y) in maxHeap]
