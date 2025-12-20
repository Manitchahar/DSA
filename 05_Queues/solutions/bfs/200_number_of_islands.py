from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Problem: 200. Number of Islands
        Link: https://leetcode.com/problems/number-of-islands/
        
        Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
        
        Time Complexity: O(m * n)
        Space Complexity: O(min(m, n)) for queue
        """
        if not grid:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visit = set()
        
        def bfs(r, c):
            q = deque()
            visit.add((r, c))
            q.append((r, c))
            
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < rows and 0 <= nc < cols and
                        grid[nr][nc] == "1" and (nr, nc) not in visit):
                        q.append((nr, nc))
                        visit.add((nr, nc))
                        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
                    
        return islands
