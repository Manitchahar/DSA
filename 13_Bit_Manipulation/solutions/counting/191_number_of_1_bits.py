class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Problem: 191. Number of 1 Bits
        Link: https://leetcode.com/problems/number-of-1-bits/
        
        Write a function that takes the binary representation of a positive integer and returns the number of set bits it has (also known as the Hamming weight).
        
        Time Complexity: O(1) - Loop runs max 32 times
        Space Complexity: O(1)
        """
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count
