"""
77. 组合
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        递归：
        1. 每次循环从指针处去除当前值，加入到path，然后当前指针+1，并和path一起传入下一次递归；
        2. 当path长度和k相等时；结果里添加path;
        """
        if k > n:
            return []
        res = []
        nums = list(range(1, n + 1))

        def backtrace(path, pointer):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(pointer, n):
                path.append(nums[i])
                backtrace(path, i+1)
                path.pop()
        backtrace([], 0)
        return res
