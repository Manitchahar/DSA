from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Problem: 66. Plus One
        Link: https://leetcode.com/problems/plus-one/
        
        You are given a large integer represented as an integer array digits/
        Increment the large integer by one and return the resulting array of digits.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Iterate backwards
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
            
        # If we are here, it means we had a carry all the way (e.g. 999 -> 000)
        return [1] + digits
