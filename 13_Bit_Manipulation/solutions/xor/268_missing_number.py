from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Problem: 268. Missing Number
        Link: https://leetcode.com/problems/missing-number/
        
        Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        res = len(nums)
        for i in range(len(nums)):
            res = res ^ i ^ nums[i]
        return res
