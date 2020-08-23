"""
153. 寻找旋转排序数组中的最小值 https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        方案1： 暴力法
        时间复杂度：O(N)
        空间复杂度：O(1)
        """
        # res = float('inf')
        # for i in nums:
        #     res = min(res, i)
        # return res

        """
        方案2：二分查找, 目标是找到【非递增的一侧】
        时间复杂度：O(logN)
        空间复杂度：O(1)
        """
        left, right = 0, len(nums) - 1
        res = float('inf')
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= nums[left]:  # mid > left， 则左侧递增，剪掉
                res = min(res, nums[left])
                left = mid + 1
            else:  # mid < left, 说明mid左侧有旋转点，剪掉右侧
                res = min(res, nums[mid])
                right = mid - 1
        return res