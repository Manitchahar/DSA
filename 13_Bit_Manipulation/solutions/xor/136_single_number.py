from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Problem: 136. Single Number
        Link: https://leetcode.com/problems/single-number/
        
        Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        res = 0
        for n in nums:
            res = res ^ n
        return res
