class Solution:
    def isValid(self, s: str) -> bool:
        """
        Problem: 20. Valid Parentheses
        Link: https://leetcode.com/problems/valid-parentheses/
        
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                # Top element element if stack is not empty, else dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the mapping for this bracket doesn't match the stack's top, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)
        
        # In the end, if the stack is empty, then we have a valid expression.
        return not stack
