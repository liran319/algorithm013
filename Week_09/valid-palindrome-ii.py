"""
680. 验证回文字符串 Ⅱ
https://leetcode-cn.com/problems/valid-palindrome-ii/
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        双指针遍历 + 字符串反转
        """
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return s[l:r] == s[l:r][::-1] or s[l+1:r+1] == s[l+1:r+1][::-1]
            l += 1
            r -= 1
        return True
