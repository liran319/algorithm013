"""
105. 从前序与中序遍历序列构造二叉树

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        '''
        递归：
        1. 先根据前序遍历，找到根节点；
        2. 然后根据中序遍历 左-中-右的次序，由于题中提到每个节点值各不相同，所以可以直接找到根节点在中序遍历的位置，则左侧是左子树，右侧是右子树；
        3. 然后根据中序左子树的长度和前序列表，定位出前、中序的左子树数组；
        4. 同理获得前、中序的右子树数组；
        5. 分别在把 3、4部中的子数组作为参数递归的调用，获得左子树和右子树，分别作为根节点的左右子树；

        时间复杂度：O(N), 每个节点遍历一次，N是二叉树所有节点的个数；
        空间复杂度：O(N), 递归的深度在O(logN) ~ O(N) 之间；树的高度在LogN到N之间，并且中间有用到存子数组，最长为N；
        '''
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])

        root_inorder_index = inorder.index(preorder[0])
        inorder_left = inorder[0:root_inorder_index]
        inorder_right = inorder[root_inorder_index + 1:]

        preorder_left = preorder[1:len(inorder_left) + 1]
        preorder_right = preorder[len(inorder_left) + 1:]

        if inorder_left and preorder_left:
            root.left = self.buildTree(preorder_left, inorder_left)
        if inorder_right and preorder_right:
            root.right = self.buildTree(preorder_right, inorder_right)
        return root
