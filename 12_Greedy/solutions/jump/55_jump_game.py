from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Problem: 55. Jump Game
        Link: https://leetcode.com/problems/jump-game/
        
        You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
        Return true if you can reach the last index, or false otherwise.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        goal = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
                
        return goal == 0
