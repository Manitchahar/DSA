from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Problem: 739. Daily Temperatures
        Link: https://leetcode.com/problems/daily-temperatures/
        
        Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([t, i])
        return res
