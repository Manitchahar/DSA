from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Problem: 200. Number of Islands
        Link: https://leetcode.com/problems/number-of-islands/
        
        Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
        
        Time Complexity: O(m * n)
        Space Complexity: O(m * n) - worse case recursion depth
        """
        if not grid:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        islands = 0
        
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                grid[r][c] == "0"):
                return
            
            grid[r][c] = "0" # Mark as visited (sink the island)
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
                    
        return islands
