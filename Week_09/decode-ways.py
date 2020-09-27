"""
91. 解码方法
https://leetcode-cn.com/problems/decode-ways/
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        """
        方案1 dp状态表
        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        # if not s:
        #     return 0
        # dp = [0] * len(s)
        # if s[0] != '0':
        #     dp[0] = 1

        # for i in range(1, len(s)):
        #     if s[i] == '0':  # 如果当前数字为0，则只有当前一个数字是1或者2的时候，才可以和前一个数字一起组成有效的两位数，且只有一种解法
        #         if s[i - 1] == '1' or s[i - 1] == '2':
        #             dp[i] = 1 if i == 1 else dp[i - 2]
        #         else:  # 否则，像 30、00 这种都是属于无效的，没有解法，直接返回0
        #             return 0
        #     else:
        #         dp[i] = dp[i - 1]  # 其他情况的时候，dp[i] 至少有一种解法是通过dp[i - 1] 走途径第i个数字到达
        #         if '10' < s[i - 1: i + 1] <= '26':  # 如果第i-1 和第 1 个数字组成的两位数是不大于 26的，那么还有另外一种解法是从第i-2个数字途径一个两位数到达
        #             dp[i] += 1 if i == 1 else dp[i - 2]
        # return dp[-1]

        """
        方案2，记忆化缓存
        因为用到的之前记录只有第 i-1 个和第 i-2 个，所以可以用类似于斐波拉切数列类似的缓存来处理
        时间复杂度：O(n)
        空间复杂度：O(1)
        """

        if not s or s[0] == '0':
            return 0

        prev, curr = 1, 1  # i - 2 和 i - 1 分别都为1
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i - 1] in ['1', '2']:  # dp[i] = dp[i - 2]
                    prev, curr = curr, prev
                else:
                    return 0
            else:
                if '10' < s[i - 1: i + 1] <= '26':
                    prev, curr = curr, prev + curr
                else:
                    prev = curr

        return curr





