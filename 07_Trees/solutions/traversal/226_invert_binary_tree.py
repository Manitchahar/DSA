from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Problem: 226. Invert Binary Tree
        Link: https://leetcode.com/problems/invert-binary-tree/
        
        Given the root of a binary tree, invert the tree, and return its root.
        
        Time Complexity: O(n)
        Space Complexity: O(h) - height of tree
        """
        if not root:
            return None
            
        # Swap children
        root.left, root.right = root.right, root.left
        
        # Recurse
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
