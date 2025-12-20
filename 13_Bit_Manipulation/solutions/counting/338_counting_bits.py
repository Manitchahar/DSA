from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Problem: 338. Counting Bits
        Link: https://leetcode.com/problems/counting-bits/
        
        Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
        
        Time Complexity: O(n)
        Space Complexity: O(1) (ignoring return array)
        """
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # i >> 1 is i // 2
            # i & 1 is i % 2
            dp[i] = dp[i >> 1] + (i & 1)
            
        return dp
