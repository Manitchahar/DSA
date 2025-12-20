from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Problem: 98. Validate Binary Search Tree
        Link: https://leetcode.com/problems/validate-binary-search-tree/
        
        Given the root of a binary tree, determine if it is a valid binary search tree (BST).
        
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
                
            return (valid(node.left, left, node.val) and 
                    valid(node.right, node.val, right))
            
        return valid(root, float("-inf"), float("inf"))
