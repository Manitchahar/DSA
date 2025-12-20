from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        Problem: 252. Meeting Rooms
        Link: https://leetcode.com/problems/meeting-rooms/
        
        Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person can attend all meetings.
        
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """
        intervals.sort()
        
        for i in range(len(intervals) - 1):
            # If current meeting ends AFTER next meeting starts
            if intervals[i][1] > intervals[i+1][0]:
                return False
                
        return True
