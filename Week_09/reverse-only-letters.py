"""
917. 仅仅反转字母
https://leetcode-cn.com/problems/reverse-only-letters/
"""

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        s, l, r = list(S), 0, len(S) - 1
        while l <= r:
            if s[l].isalpha() and s[r].isalpha():
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[l].isalpha():
                r -= 1
            else:
                l += 1
        return ''.join(s)
