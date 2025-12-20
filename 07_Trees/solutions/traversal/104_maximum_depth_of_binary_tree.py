from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Problem: 104. Maximum Depth of Binary Tree
        Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
        
        Given the root of a binary tree, return its maximum depth.
        
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        if not root:
            return 0
            
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
