from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Problem: 994. Rotting Oranges
        Link: https://leetcode.com/problems/rotting-oranges/
        
        Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
        
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        time = 0
        
        # 1. Initialize Queue with all originally rotten oranges and count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
                    
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        # 2. BFS
        while q and fresh > 0:
            # Complete one "minute" or level
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    # If in bounds and fresh, rot it
                    if (0 <= row < rows and 0 <= col < cols and
                        grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1
            
        return time if fresh == 0 else -1
