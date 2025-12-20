from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Problem: 22. Generate Parentheses
        Link: https://leetcode.com/problems/generate-parentheses/
        
        Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
        
        Time Complexity: O(4^n / sqrt(n)) - Catalan number
        Space Complexity: O(n) for stack depth
        """
        # Only add open parenthesis if open < n
        # Only add closing parenthesis if closed < open
        # Valid IIF open == closed == n
        
        stack = []
        res = []
        
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
                
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
                
        backtrack(0, 0)
        return res
