from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Problem: 253. Meeting Rooms II
        Link: https://leetcode.com/problems/meeting-rooms-ii/
        
        Given an array of meeting time intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
        
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])
        
        res, count = 0, 0
        s, e = 0, 0
        
        while s < len(intervals):
            # A meeting started before one ended -> Need a Room
            if starts[s] < ends[e]:
                s += 1
                count += 1
            # A meeting ended -> Free up a Room
            else:
                e += 1
                count -= 1
                
            res = max(res, count)
            
        return res
