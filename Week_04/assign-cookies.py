"""
455. 分发饼干

"""

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        先排序，然后贪心算法，每次优先挑选刚好满足条件的饼干先发掉
        时间复杂度：O(mlogm + nlogn + m + n), m/n 分别为g和s的长度
        空间复杂度：O(1)
        """
        if not g or not s:
            return 0
        g.sort()
        s.sort()
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
            j += 1
        return i

