"""
52. N皇后 II
https://leetcode-cn.com/problems/n-queens-ii/
"""

class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        只用统计符合条件的总数的话，可以使用位运算的dfs
        """
        if n < 1:
            return []
        self.count = 0

        def dfs(row, cols, pies, nas):
            if row == n:
                self.count += 1
                return
            bits = ~(cols | pies | nas) & ((1 << n) - 1)  # 取得目前所有列、撇、捺所占用的位置、取反，然后和11111111 按位与，得到目前当前行 row 所有可用的空位
            while bits:
                p = bits & -bits  # 获取最低位的p，用来存放Q
                bits = bits & (bits - 1)  # 存放Q后，将p所在的位置（最低位的1）清零
                dfs(row + 1, cols | p, (pies | p) << 1, (nas | p) >> 1)

        dfs(0, 0, 0, 0)
        return self.count
