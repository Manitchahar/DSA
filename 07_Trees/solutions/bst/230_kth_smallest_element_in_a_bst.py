from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Problem: 230. Kth Smallest Element in a BST
        Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
        
        Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
        
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        stack = []
        curr = root
        
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
                
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
                
            curr = curr.right
            
        return -1
