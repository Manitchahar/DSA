from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Problem: 39. Combination Sum
        Link: https://leetcode.com/problems/combination-sum/
        
        Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target.
        The same number may be chosen from candidates an unlimited number of times.
        
        Time Complexity: O(2^t) where t is target value
        Space Complexity: O(t)
        """
        res = []
        
        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            # Decision 1: Include candidates[i] (and stay at i to reuse it)
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])
            
            # Decision 2: Context switch, don't use candidates[i] anymore
            curr.pop()
            dfs(i + 1, curr, total)
            
        dfs(0, [], 0)
        return res
