from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Problem: 300. Longest Increasing Subsequence
        Link: https://leetcode.com/problems/longest-increasing-subsequence/
        
        Given an integer array nums, return the length of the longest strictly increasing subsequence.
        
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        if not nums:
            return 0
            
        dp = [1] * len(nums)
        
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    
        return max(dp)
