'''
242. 有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        存一个字典，键值分别为字符串-出现的次数，s中字母次数+1，t中字母次数-1
        时间复杂度O(m+n), m, n 分别为s和t的长度
        空间复杂度O(1)， 因为题目中只包含26个英文字母
        '''
        if len(s) != len(t):
            return False

        hashmap = {}
        for i in s:
            hashmap[i] = hashmap.get(i, 0) + 1
        print(hashmap)
        for j in t:
            count = hashmap.get(j, 0)
            if count == 0:
                return False
            else:
                hashmap[j] = count - 1
        return True