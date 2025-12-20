from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Problem: 435. Non-overlapping Intervals
        Link: https://leetcode.com/problems/non-overlapping-intervals/
        
        Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
        
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        
        for start, end in intervals[1:]:
            if start >= prevEnd:
                # No overlap
                prevEnd = end
            else:
                # Overlap: Remove the one that ends later (keeping the one that ends sooner opens up more space)
                res += 1
                prevEnd = min(prevEnd, end)
                
        return res
