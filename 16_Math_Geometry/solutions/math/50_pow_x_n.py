class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Problem: 50. Pow(x, n)
        Link: https://leetcode.com/problems/powx-n/
        
        Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
        
        Time Complexity: O(log n)
        Space Complexity: O(log n) stack
        """
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1
            
            res = helper(x, n // 2)
            res = res * res
            return x * res if n % 2 else res
            
        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res
