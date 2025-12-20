class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        Problem: 371. Sum of Two Integers
        Link: https://leetcode.com/problems/sum-of-two-integers/
        
        Given two integers a and b, return the sum of the two integers without using the operators + and -.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # Python integers are arbitrarily large, so we need a mask to assume 32-bit
        mask = 0xffffffff
        
        while (b & mask) > 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
            
        # Handle overflow/negative numbers for Python
        return (a & mask) if b > 0 else a
