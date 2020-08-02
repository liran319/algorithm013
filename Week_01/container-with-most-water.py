class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        方案1：暴力求解。两层循环，各自求出前后两个值所对应的面积，取最大值
        时间复杂度：O(n^2)
        空间复杂度：O(1)
        提交结果：超出时间限制
        '''
        # area = 0
        # for i in range(len(height) - 1):
        #     for j in range(i + 1, len(height)):
        #         area = max(area, (j - i) * min(height[i], height[j]))
        # return area

        '''
        方案2：夹逼求解。前后两个指针，各自对应的值小的移动，指针向中间移动
        时间复杂度: O(n)
        空间复杂度: O(1)
        '''
        area, start, end = 0, 0, len(height) - 1
        while start < end:
            if height[start] < height[end]:
                area = max(area, (end - start) * height[start])
                start += 1
            else:
                area = max(area, (end - start) * height[end])
                end -= 1
        return area


