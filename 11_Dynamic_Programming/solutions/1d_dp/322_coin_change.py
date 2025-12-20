from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Problem: 322. Coin Change
        Link: https://leetcode.com/problems/coin-change/
        
        Return the fewest number of coins that you need to make up that amount.
        
        Time Complexity: O(amount * len(coins))
        Space Complexity: O(amount)
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    
        return dp[amount] if dp[amount] != float('inf') else -1
