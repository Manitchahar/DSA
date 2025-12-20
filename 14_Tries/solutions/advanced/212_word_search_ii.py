from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Problem: 212. Word Search II
        Link: https://leetcode.com/problems/word-search-ii/
        
        Given an m x n board of characters and a list of strings words, return all words on the board.
        
        Time Complexity: O(m * n * 4^L) worst case, but optimized with Trie.
        """
        root = TrieNode()
        for w in words:
            root.addWord(w)
            
        rows, cols = len(board), len(board[0])
        res = set()
        visit = set()
        
        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                (r, c) in visit or board[r][c] not in node.children):
                return
            
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            
            if node.endOfWord:
                res.add(word)
                # Optimization: Mark false so we don't add duplicates or re-process
                node.endOfWord = False 
                
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            
            visit.remove((r, c))
            
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
                
        return list(res)
