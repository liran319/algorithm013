"""
46. 全排列
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        """
        DFS
        """
        res = []
        visited = {}
        def dfs(path):
            if len(path) == len(nums):
                res.append(path)
                return
            for i in range(len(nums)):
                if visited.get(nums[i], False) == True:
                    continue
                visited[nums[i]] = True
                dfs(path + [nums[i]])
                visited[nums[i]] = False
        dfs([])
        return res
