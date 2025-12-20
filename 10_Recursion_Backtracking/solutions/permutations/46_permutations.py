from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Problem: 46. Permutations
        Link: https://leetcode.com/problems/permutations/
        
        Given an array nums of distinct integers, return all the possible permutations.
        
        Time Complexity: O(n! * n)
        Space Complexity: O(n)
        """
        res = []
        
        # Initial call
        if len(nums) == 1:
            return [nums.copy()]
            
        for i in range(len(nums)):
            n = nums.pop(0) # Remove one element
            perms = self.permute(nums) # Get perms of the rest
            
            for p in perms:
                p.append(n) # Add removed element back
            res.extend(perms)
            
            nums.append(n) # Backtrack: add it back for next iteration
            
        return res
