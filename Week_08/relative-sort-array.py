"""
1122. 数组的相对排序
https://leetcode-cn.com/problems/relative-sort-array/
"""

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """
        采用计数排序和哈希表，先将arr1中按照arr2的顺序，找出匹配的数字进行按次排列，然后把剩下的数字进行排序
        """
        hashmap = {}
        for num in arr1:  # 将arr1的所有数字进行计数，统计在hashmap里
            if num not in hashmap:
                hashmap[num] = 0
            hashmap[num] += 1
        i = 0
        while i < len(arr1):
            for num in arr2:
                while hashmap[num] > 0:
                    arr1[i] = num
                    hashmap[num] -= 1
                    i += 1
                del hashmap[num]

        # 统计排序hashmap里剩下的数字
            rest = []
            for (key, value) in hashmap.items():
                rest += [key] * value
            rest.sort()
            for num in rest:
                arr1[i] = num
                i += 1
        return arr1