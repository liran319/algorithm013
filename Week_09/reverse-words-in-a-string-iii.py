"""
557. 反转字符串中的单词 III
https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/

示例：

输入："Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(substr[::-1] for substr in s.split())