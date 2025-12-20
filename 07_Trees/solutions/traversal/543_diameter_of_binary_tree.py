from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Problem: 543. Diameter of Binary Tree
        Link: https://leetcode.com/problems/diameter-of-binary-tree/
        
        Given the root of a binary tree, return the length of the diameter of the tree.
        The diameter is the length of the longest path between any two nodes in a tree.
        
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        self.res = 0
        
        def dfs(curr):
            if not curr:
                return 0
                
            left = dfs(curr.left)
            right = dfs(curr.right)
            
            # Update max diameter (path through current node)
            self.res = max(self.res, left + right)
            
            # Return height
            return 1 + max(left, right)
            
        dfs(root)
        return self.res
