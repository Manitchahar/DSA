from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Problem: 45. Jump Game II
        Link: https://leetcode.com/problems/jump-game-ii/
        
        Return the minimum number of jumps to reach the last index.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        res = 0
        l = r = 0
        
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
            
        return res
