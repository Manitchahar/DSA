from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Problem: 73. Set Matrix Zeroes
        Link: https://leetcode.com/problems/set-matrix-zeroes/
        
        Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
        You must do it in place.
        
        Time Complexity: O(m * n)
        Space Complexity: O(1)
        """
        rows, cols = len(matrix), len(matrix[0])
        rowZero = False # Extra variable for the first row intersection
        
        # 1. Determine which rows/cols need to be zero
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
                        
        # 2. Zero out most of the matrix (skipping first row/col)
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
                    
        # 3. Zero out first col if needed
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
                
        # 4. Zero out first row if needed
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0
