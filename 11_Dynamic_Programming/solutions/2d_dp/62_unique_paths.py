class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Problem: 62. Unique Paths
        Link: https://leetcode.com/problems/unique-paths/
        
        There is a robot on an m x n grid. The robot is initially located at the top-left corner (0, 0).
        The robot tries to move to the bottom-right corner (m - 1, n - 1). 
        The robot can only move either down or right at any point in time.
        
        Time Complexity: O(m * n)
        Space Complexity: O(n) (Optimized from O(m*n))
        """
        row = [1] * n
        
        # Go through rows (except the last one which is all 1s)
        for i in range(m - 1):
            newRow = [1] * n
            # Go backwards
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
            
        return row[0]
