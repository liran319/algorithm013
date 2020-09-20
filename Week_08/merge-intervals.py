"""
56. 合并区间
https://leetcode-cn.com/problems/merge-intervals/
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        时间复杂度：O(NlogN + N), 分别为排序和合并的复杂度
        空间复杂度：O(logN) 排序所需要的空间
        '''
        intervals.sort(key=lambda x: x[0])  # 将intervas按照区间起始点进行排序
        res = []
        for item in intervals:
            if not res or item[0] > res[-1][1]:  # 如果当前区间起始点比上一个区间的结束点要大，说明没有交集，则添加为新的区间
                res.append(item)
            else:  # 否则，合并当前区间到结果中的上一个区间，合并后的区间结尾取两者最大值
                res[-1][1] = max(res[-1][1], item[1])
        return res