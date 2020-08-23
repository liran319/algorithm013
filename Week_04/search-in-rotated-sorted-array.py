"""
33. 搜索旋转排序数组 https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        暴力解法：从头到尾遍历
        时间复杂度：O(N)
        空间复杂度：O(1)
        """
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1


        """
        二分查找
        1. 先根据left、mid、right所在的值比较，判断哪半边有序，哪半边无序；
        2. 先判断有序的半边里是否包含target，有的话，就减掉无序的半边，接下去进行二分搜索；
        3. 反之，减掉有序的半边，对剩下的无序半边进行上述1、2步的二分查找；
        时间复杂度：O(logN)
        空间复杂度：O(1)
        """
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # 先判断那半边有序，那半边无序，然后根据有序的一边比较target和两端值，减去半边
            if nums[left] <= nums[mid]:  # 左半边有序，右半边无序
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:   # 左半边无序，右半边有序
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1





