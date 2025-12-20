from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Problem: 102. Binary Tree Level Order Traversal
        Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
        
        Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
        
        Time Complexity: O(n)
        Space Complexity: O(n) (max width of tree)
        """
        if not root:
            return []
            
        res = []
        q = deque([root])
        
        while q:
            level = []
            qLen = len(q) # Snapshot of current level size
            
            for _ in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
            
            if level:
                res.append(level)
                
        return res
