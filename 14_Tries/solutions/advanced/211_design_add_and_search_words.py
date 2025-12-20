class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    """
    Problem: 211. Design Add and Search Words Data Structure
    Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/
    
    Design a data structure that supports adding new words and finding if a string matches any previously added string.
    The search word can contain the dot character '.' to represent any one letter.
    """

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            cur = root
            
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    # Backtracking: Check all possible children
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
                    
            return cur.endOfWord
        
        return dfs(0, self.root)
