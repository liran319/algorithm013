"""
51. N 皇后
https://leetcode-cn.com/problems/n-queens/
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        利用set的dfs解法
        """
        res, cols, pies, nas = [], set(), set(), set()

        def dfs(path, row):
            if len(path) == n:
                res.append(path)
                return
            for col in range(n):
                if col in cols or (col - row) in pies or (col + row) in nas:
                    continue
                cols.add(col)
                pies.add(col - row)
                nas.add(col + row)

                dfs(path + ['.' * col + 'Q' + '.' * (n - 1 - col)], row + 1)

                nas.remove(col + row)
                pies.remove(col - row)
                cols.remove(col)
        dfs([], 0)
        return res
