'''
    # N: number of words
    # l: length of words
    # sizeOfAlphabet = 26
    
    Space Complexity: O(N*l*26)
    
    Time Complexities:
    Insert: O(l)
    Initialize: O(26)
    Search: O(l)
    StartsWith: O(p) #p = size of prefix
'''
class Trie:
    class Node:
        def __init__(self, val):
            self.val = val
            self.childern = [None]*26
            self.isLeaf = False

    def __init__(self):
        self.tree = [None] * 26
        

    def insert(self, word: str) -> None:
        if self.tree[ord(word[0]) - ord('a')]: cur = self.tree[ord(word[0]) - ord('a')]
        else: cur = self.tree[ord(word[0]) - ord('a')] = Trie.Node(word[0])
        for c in word[1:]:
            if not cur.childern[ord(c) - ord('a')]:
                cur.childern[ord(c) - ord('a')] = Trie.Node(c)
            cur = cur.childern[ord(c) - ord('a')]
        cur.isLeaf = True
        

    def search(self, word: str) -> bool:
        cur = self.tree[ord(word[0]) - ord('a')]
        for c in word[1:]:
            if not cur: return False
            cur = cur.childern[ord(c) - ord('a')]
        return cur and cur.isLeaf
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.tree[ord(prefix[0]) - ord('a')]
        for c in prefix[1:]:
            if not cur: return False
            cur = cur.childern[ord(c) - ord('a')]
        return cur
