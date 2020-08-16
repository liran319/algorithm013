'''
26. 删除排序数组中的重复项

给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。


示例 1:
给定数组 nums = [1,1,2],
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
你不需要考虑数组中超出新长度后面的元素。

示例 2:
给定 nums = [0,0,1,1,1,2,2,3,3,4],
函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
你不需要考虑数组中超出新长度后面的元素。
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        方案：指针。
        思路：既然是个排序数组，那么只需要比较相邻两个指针i, j 所对应的数字是否相等，如果相等，则删除j所在的元素，i, j 不变，继续比较
        时间复杂度：nO(n)
        空间复杂度：O(1)
        '''
        # if len(nums) <= 1:
        #     return len(nums)
        # i = 0
        # while i < len(nums) - 1:
        #     j = i + 1
        #     if nums[i] == nums[j]:
        #         del nums[j]
        #     else:
        #         i += 1
        # return len(nums)

        '''
        方案2：快慢指针
        思路：题目中说到【你不需要考虑数组中超出新长度后面的元素。】，也就是只要保证数组前k个元素是不重复的就可以，其中k为本题去重数组的长度。
        j——慢指针，i——快指针，一旦两数相等，则i增加，去查找下一个数字，直到找到不同的数字，j+1出保存为i的值，直到循环解除
        '''
        i, j = 1, 0
        while i < len(nums):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]
            i += 1
        return j + 1