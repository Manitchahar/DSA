from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Problem: 1. Two Sum
        Link: https://leetcode.com/problems/two-sum/
        
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        prevMap = {} # val : index
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return []
