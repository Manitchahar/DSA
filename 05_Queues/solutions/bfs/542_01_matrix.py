from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Problem: 542. 01 Matrix
        Link: https://leetcode.com/problems/01-matrix/
        
        Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
        
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """
        rows, cols = len(mat), len(mat[0])
        q = deque()
        
        # Initialize queue with all 0s, set others to infinity
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1 # Unvisited
                    
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while q:
            r, c = q.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[r][c] + 1
                    q.append((nr, nc))
                    
        return mat
