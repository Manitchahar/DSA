from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Problem: 56. Merge Intervals
        Link: https://leetcode.com/problems/merge-intervals/
        
        Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
        
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        if not intervals:
            return []
            
        # 1. Sort by start time
        intervals.sort(key=lambda x: x[0])
        
        output = [intervals[0]]
        
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            
            if start <= lastEnd:
                # Merge logic: end is the max of both
                output[-1][1] = max(lastEnd, end)
            else:
                # No overlap, add to output
                output.append([start, end])
        
        return output
