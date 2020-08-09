
'''
589. N叉树的前序遍历

'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        '''
        方案：递归
        时间复杂度：O(n)
        空间复杂度：O(k)，k为N叉树的层数
        '''
        res = []
        def helper(_root):
            if not _root:
                return None
            res.append(_root.val)
            for child in _root.children:
                helper(child)
        helper(root)
        return res
