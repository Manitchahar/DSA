class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Problem: 190. Reverse Bits
        Link: https://leetcode.com/problems/reverse-bits/
        
        Reverse bits of a given 32 bits unsigned integer.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        res = 0
        
        for i in range(32):
            bit = (n >> i) & 1 # Get ith bit
            res = res | (bit << (31 - i)) # Place it in reverse spot
            
        return res
