class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Problem: 72. Edit Distance
        Link: https://leetcode.com/problems/edit-distance/
        
        Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
        
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """
        cache = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]
        
        # Base cases: empty string to other string requires len(other) inserts
        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i
            
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                    cache[i][j] = 1 + min(
                        cache[i+1][j],    # Delete
                        cache[i][j+1],    # Insert
                        cache[i+1][j+1]   # Replace
                    )
                    
        return cache[0][0]
