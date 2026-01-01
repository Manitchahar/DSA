from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Problem: 48. Rotate Image
        Link: https://leetcode.com/problems/rotate-image/
        
        You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
        You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
        
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        n = len(matrix)
        
        # 1. Transpose (Swap across diagonal)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        # 2. Reverse each row
        for i in range(n):
            matrix[i].reverse()
