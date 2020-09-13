"""
547. 朋友圈
https://leetcode-cn.com/problems/friend-circles/
"""

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        """
        并查集
        1. 构建初始状态的p，m个元素各自独自成为一个集合，p[i] = i;
        2. 创建查找代表代表(_findParent), 合并函数(_union);
        3. 遍历矩阵，找到符合 M[i][j]的元素，并将i, j 各自所在集合合并。又因为M[i][j] == M[j][i], 意思是 i 和 j是朋友，就等于 j和i 也是朋友，所以只需要遍历一半的矩阵；
        4. 最后遍历 m个元素，找到各自所在圈子的代表，用set去重后，取得长度，即为结果。
        """
        m = len(M)
        p = [i for i in range(m)]

        def _findParent(p, i):
            root = i
            while p[root] != root:
                root = p[root]
            return root

        def _union(p, i, j):
            pi, pj = _findParent(p, i), _findParent(p, j)
            p[pj] = pi

        for i in range(m - 1):
            for j in range(i + 1, m):
                if M[i][j] == 1:
                    _union(p, i, j)

        return len(set([_findParent(p, i) for i in range(m)]))

