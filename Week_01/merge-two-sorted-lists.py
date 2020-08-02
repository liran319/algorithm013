'''
21. 合并两个有序链表

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。  

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        双指针：比较l1 和 l2当前节点的值，选择较小的放在前面
        时间复杂度：O(n)
        空间复杂度：O(1)
        '''
        if not l1 and not l2:
            return None
        tmp = ListNode(0)  # 因为不知道两个链表第一个节点大小，所以需要创建一个第0个节点，指向排序后的链表
        res = tmp
        while l1 or l2:
            if not l1:  # 如果一个链表遍历完了，next指向另外一个链表剩下的部分，并结束循环，返回结果
                tmp.next = l2
                break
            if not l2:  # 如果一个链表遍历完了，next指向另外一个链表剩下的部分，并结束循环，返回结果
                tmp.next = l1
                break
            if l1.val < l2.val:  # 节点数值小的链表，指针加1
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        return res.next



