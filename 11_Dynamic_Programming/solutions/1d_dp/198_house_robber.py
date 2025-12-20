from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Problem: 198. House Robber
        Link: https://leetcode.com/problems/house-robber/
        
        You are a professional robber planning to rob houses along a street. 
        Adjacent houses have security systems connected.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        rob1, rob2 = 0, 0
        
        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
            
        return rob2
