"""
151. 翻转字符串里的单词
https://leetcode-cn.com/problems/reverse-words-in-a-string/
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.strip().split()[::-1])