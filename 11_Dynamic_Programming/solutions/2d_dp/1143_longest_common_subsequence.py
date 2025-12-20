class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Problem: 1143. Longest Common Subsequence
        Link: https://leetcode.com/problems/longest-common-subsequence/
        
        Given two strings text1 and text2, return the length of their longest common subsequence.
        
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """
        # 2D Grid initialized with 0s
        # Dimensions: (len(text1) + 1) x (len(text2) + 1)
        dp = [[0 for j in range(len(text2) + 1)] 
                 for i in range(len(text1) + 1)]
                 
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    # Match: 1 + diagonal
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    # No Match: Max of right or down
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
                    
        return dp[0][0]
