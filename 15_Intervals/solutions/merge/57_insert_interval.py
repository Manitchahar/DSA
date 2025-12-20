from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Problem: 57. Insert Interval
        Link: https://leetcode.com/problems/insert-interval/
        
        Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals is still formed by non-overlapping intervals (merge if necessary).
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        res = []
        
        for i in range(len(intervals)):
            # If new interval is BEFORE current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            # If new interval is AFTER current interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
                
            # If overlap, merge them into newInterval
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
                
        res.append(newInterval)
        return res
