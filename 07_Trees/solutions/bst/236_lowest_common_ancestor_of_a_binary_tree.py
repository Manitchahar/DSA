from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Problem: 236. Lowest Common Ancestor of a Binary Tree
        Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
        
        Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
        
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        if not root or root == p or root == q:
            return root
            
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right return a node, then current root is the LCA
        if left and right:
            return root
            
        # Otherwise, return the one that found something (or None)
        return left or right
