'''
429. N叉树的层序遍历
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        '''
        使用队列queue来存储【同一层的节点】。
        遍历该层节点，val添加到该层的结果中，顺便把该层每个child节点添加到queue末尾，以便进行下一层遍历。
        时间复杂度：O(n), 每个节点只遍历一次
        空间复杂度：O(n), 最坏情况下，所有n-1 个child节点都位于 root节点的下一层
        '''
        if not root:
            return []
        res = []
        queue = [root]
        while queue:  # 一直循环到queue被遍历完
            tmp = []  # 每一层的结果保存到一个单独的数组里
            for i in range(len(queue)):
                # queue为当前层的所有子节点，所以遍历次数为len(queue), 完成后queue可以不为空，
                # 因为每个节点的children也会不断的推到 queue里
                cur = queue.pop(0)  # 取出队列的第一个节点，如果为空，直接跳过，去遍历下一个节点
                if not cur:
                    continue
                tmp.append(cur.val)  # 每遍历一个node，都把val推到tmp里
                if not cur.children:
                    continue
                for j in cur.children:
                    queue.append(j)
            res.append(tmp)  # 当前层节点的值都添加完成后，把当前层结果保存，进行下一层的遍历
        return res