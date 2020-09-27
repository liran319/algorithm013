"""
387. 字符串中的第一个唯一字符
https://leetcode-cn.com/problems/first-unique-character-in-a-string/
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for i in s:
            hashmap[i] = hashmap.get(i, 0) + 1

        for (k, v) in hashmap.items():
            if v == 1:
                return s.find(k)
        return -1