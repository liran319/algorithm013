"""
208. 实现 Trie (前缀树)
"""

class TreeNode:
    def __init__(self, val=None, is_end=False):
        self.val = val
        self.next = {}
        self.is_end = is_end


class Trie:
    def __init__(self):
        self.node = TreeNode()

    def insert(self, word: str) -> None:
        tmp = self.node
        for i in word:
            if i not in tmp.next:
                tmp.next[i] = TreeNode(i)
            tmp = tmp.next[i]
        tmp.is_end = True

    def search(self, word: str):
        tmp = self.node
        for i in word:
            if i not in tmp.next:
                return False
            tmp = tmp.next[i]
        return tmp.is_end

    def startsWith(self, prefix: str):
        tmp = self.node
        for i in prefix:
            if i not in tmp.next:
                return False
            tmp = tmp.next[i]
        return True



