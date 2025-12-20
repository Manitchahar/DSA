from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Problem: 150. Evaluate Reverse Polish Notation
        Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/
        
        Evaluate the value of an arithmetic expression in Reverse Polish Notation.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a)) # Truncate toward zero
            else:
                stack.append(int(c))
        return stack[0]
