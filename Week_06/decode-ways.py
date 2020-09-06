"""
91. 解码方法
https://leetcode-cn.com/problems/decode-ways/
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        方案：动态规划
        输入："2163"
        等同于 ('2' + '1') * dp('63') + ('21') + dp('63')
        dp[i] = fn(i) * dp[i - 1] + dp[i - 2] * fn(i - 1, i)
        '''
        size = length = len(s)
        dp = [0 for i in s]
        if s[0] != '0':
            dp[0] = 1
        for i in range(1, length):
            if s[i] != '0':
                dp[i] = dp[i - 1]
            if '10' <= s[i-1: i+1] <= '26':
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i - 2]
        return dp[-1]
