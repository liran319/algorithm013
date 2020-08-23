"""
55. 跳跃游戏
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        动态规划
        记录从前面所有元素出发的可能性，但是复杂度过高，因为每个元素都可能再遍历一次
        时间复杂度：O(n^2)
        空间复杂度：O(n), n 为 nums长度
        """
        # length, i, res = len(nums), 0, False
        # dp = [0] * length
        # dp[0] = True
        # for i in range(1, length):
        #     res = False
        #     for j in range(i):
        #         if dp[j] == True and (j + nums[j] >= i):
        #             res = True
        #             break

        #     dp[i] = res
        # return dp[length - 1]

        """
        迭代法
        依次尽量遍历数组中可到达的元素集合，记录每一次从当前元素跳跃，能到达的最远点，并更新能全局到达的最远的元素
        时间复杂度：O(n)
        空间复杂度：O(1)
        """

        i, longest = 0, 0
        while i < len(nums):
            if i <= longest:
                longest = max(longest, i + nums[i])
            i += 1
        return longest >= len(nums) - 1

