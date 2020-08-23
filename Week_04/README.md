学习笔记

### DFS
1. 递归
```python
def dfs(root):
  visited = set()
  for child in root.children:
    if child not in visited:
      visited.add(child)
      dfs(child)
```
2. 迭代
```python
def dfs(root):
  visited, stack = set(), [root]
  while stack:
    node = stack.pop()
    if node not in visited:
      visited.add(node)
      for child in node.children:
        stack.insert(0, child)
```

### BFS
```python
def bfs(root):
  visited = set()
  queue = [root]
  while queue:
    node = queue.pop()
    visited.add(node)
    for child in node.children:
      queue.append(child)
```

### 贪心算法
1. 贪心算法的特点是每一步都进行当前步骤的最优解，也就是局部最优解；
2. 贪心算法的局部最优解，不一定能获得全局的最优解；
3. 贪心算法是在每一步都进行局部最优的选择，并且结果不能回退；而动态规划是保存之前的结果，并且根据之前保存的结果，对当下进行选择，并且可以回退，取最优结果。


### 二分查找
#### 特点
1. 递增或有序
2. 有边界
3. 能通过索引（下标）访问；

#### 应用
`使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方`

输入 `[4, 5, 6, 7, 0, 1, 2]`,

输出 `0`（旋转的起始点）

* 方案1：遍历，时间复杂度O(N), 空间复杂度：O(1)
  ```python
  def fn(nums):
      if not nums:
          return None
      for i in range(1, len(nums)):
          if nums[i] < nums[i - 1]:  # 如果当前元素比前一个小，说明当前点是旋转点，中断循环，返回结果
              return nums[i]

  ```

* 和搜索旋转数组类似，要找到旋转点, 就是不断的剪掉单调递增的一侧;
  终止循环的条件是 left + 1 == right, 且 nums[left] > nums[right]
  时间复杂度：O(logN)
  空间复杂度：O(1)

```python
def fn(nums):
    if not nums:
        return None
    left, right = 0, len(nums) - 1
    res = 0
    while left <= right:
        mid = (left + right) // 2
        if nums[left] < nums[mid] < nums[right]:
            return nums[left]
        if left == right - 1 and nums[left] > nums[right]:
            return nums[right]
        if nums[mid] <= nums[left]:  # mid <= left, 则右侧肯定是单调递增的，剪掉mid 右侧
            right = mid
        else:  # mid > left, 左侧肯定递增，剪掉mid的左侧
            left = mid
    return nums[res]

```
