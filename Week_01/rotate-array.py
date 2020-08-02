'''
189. 旋转数组
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]

示例 2:
输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释:
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]

说明:
尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的 原地 算法。
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        方案1：k次步长为1的移动
        时间复杂度：O(k*n)
        空间复杂度：O(1)
        """
        # l = len(nums)
        # for i in range(k):
        #     j = l - 1
        #     tmp = nums[j]  # 暂存最后一个元素，然后剩下的元素，从后依次往前更新

        #     while j > 0:
        #         nums[j] = nums[j - 1]
        #         j -= 1
        #     nums[0] = tmp
        # return nums

        '''
        方法2：多次反转。先整体反转，然后后k个和前l - k 个依次反转
        时间复杂度：O(2n)
        空间复杂度：O(1)
        '''
        l = len(nums)  # list总长度
        if k % l == 0:  # 如果旋转的步数是总长度的倍数，相当于没旋转，直接返回原数组
            return nums
        k %= l  # 预处理下k，只取相同效果的最小旋转步数
        def reverseList(lst, start, end):
            if start == end:
                return None
            while start < end:
                lst[start], lst[end] = lst[end], lst[start]
                start += 1
                end -= 1
            print(nums)

        reverseList(nums, 0, l - 1)
        reverseList(nums, 0, k - 1)
        reverseList(nums, k, l - 1)
        return nums


