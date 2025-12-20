class TrieNode:
    def __init__(self):
        self.children = {} # Map char -> TrieNode
        self.endOfWord = False

class Trie:
    """
    Problem: 208. Implement Trie (Prefix Tree)
    Link: https://leetcode.com/problems/implement-trie-prefix-tree/
    
    A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings.
    
    Time Complexity: O(m) for all ops, where m is key length.
    Space Complexity: O(m)
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
