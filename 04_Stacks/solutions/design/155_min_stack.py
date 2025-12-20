class MinStack:
    """
    Problem: 155. Min Stack
    Link: https://leetcode.com/problems/min-stack/
    
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
    
    Time Complexity: O(1) for all operations.
    Space Complexity: O(n)
    """

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
