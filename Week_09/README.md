## 不同路径的动态规划思路

1. 首先考虑不包含障碍物的情况，以 `3 x 3` 的棋盘为例先画出dp table：
    ```
    [
      [0,0,0],
      [0,0,0],
      [0,0,0]
    ]
    ```
    因为行进只能往右或往下，以 (0, 0)为原点，`第一行`和`第一列`的其他节点，都只有一个路径（都是从它的`左边`或者`上面`的节点`向右`或`向下`而来，所以第一行和第二行的dp表的值均为1，所以dp表的初始状态为：
    | | j = 0  | j = 1  | j = 2 |
    |---|---|---|---|
    | i = 0 | 1 | 1 | 1 |
    | i = 1 | 1 |   |   |
    | i = 2 | 1 |   |   |

    考虑到 i == j == 1的情况，从(0, 0)到达它(1, 1)路径有两个，分别是从(0, 1)往下、从(1, 0)往右，所以状态表更新为：

    | | j = 0  | j = 1  | j = 2 |
    |---|---|---|---|
    | i = 0 | 1 | 1 | 1 |
    | i = 1 | 1 | d[0][1] + dp[1][0] |   |
    | i = 2 | 1 |   |   |

    同理，其他节点的dp值为

    | | j = 0  | j = 1  | j = 2 |
    |---|---|---|---|
    | i = 0 | 1 | 1 | 1 |
    | i = 1 | 1 | dp[0][1] + dp[1][0] | dp[0][2] + dp[1][1] |
    | i = 2 | 1 | dp[1][1] + dp[2][0] | dp[1][2] + dp[2][1] |

    由此可以归纳，dp方程为：
    ```python
    if i == 0 or j == 0: dp[i][j] = 1
    else: dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    ```
2. 考虑有障碍物的情况：
    ```
    [
      [0, 1, 0],
      [0, 1, 0],
      [0, 0, 0]
    ]
    ```
    如果路径上有遇到障碍物`'1'`的时候,这条路径就是不通的，所以初始状态的时候，第一行和第一列，需要根据(0, 0)和本行、本列中遍历有没有遇到，因为(0, 1)是障碍物，所以`dp[0][1] = 0`, 也顺道导致`dp[0][2] = 0`;
    | | j = 0  | j = 1  | j = 2 |
    |---|---|---|---|
    | i = 0 | 1 | 0 | 0 |
    | i = 1 | 1 |   |   |
    | i = 2 | 1 |   |   |

    (1, 1) 也是障碍物，所以`dp[1][1] = 0`，`dp[1][2] = 0`;
    到达(2,1)只有一条通路即从(2,0)向右一步到达，`dp[2][1] = dp[2][0]`,并依次类推，`dp[2][2]`也是1；

    | | j = 0  | j = 1  | j = 2 |
    |---|---|---|---|
    | i = 0 | 1 | 0 | 0 |
    | i = 1 | 1 | 0 | 0 |
    | i = 2 | 1 | dp[2][0] + 0 | dp[2][1] + 0  |

    所以它的状态方程为：
    ```python
    if i == j == 0: dp[i][j] = 1 if grid[0][0] == 0 else 0
    elif i == 0: dp[i][j] = dp[i][j - 1] if grid[i][j] == 0 else 0
    elif j == 0: dp[i][j] = dp[i - 1][j] if grid[i][j] == 0 else 0
    else: dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) if grid[i][j] == 0 else 0
    ```
    最终的解法是：
    ```python
    class Solution:
        def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
            if not obstacleGrid or not obstacleGrid[0]:
                return 0
            m, n = len(obstacleGrid), len(obstacleGrid[0])
            dp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i == j == 0: dp[i][j] = 1 if obstacleGrid[0][0] == 0 else 0
                    elif i == 0: dp[i][j] = dp[i][j - 1] if obstacleGrid[i][j] == 0 else 0
                    elif j == 0: dp[i][j] = dp[i - 1][j] if obstacleGrid[i][j] == 0 else 0
                    else: dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) if obstacleGrid[i][j] == 0 else 0
            return dp[-1][-1]
    ```

## 解码方法

```python
"""
方案1 dp状态表
时间复杂度：O(n)
空间复杂度：O(n)
"""
if not s:
    return 0
dp = [0] * len(s)
if s[0] != '0':
    dp[0] = 1

for i in range(1, len(s)):
    if s[i] == '0':  # 如果当前数字为0，则只有当前一个数字是1或者2的时候，才可以和前一个数字一起组成有效的两位数，且只有一种解法
        if s[i - 1] == '1' or s[i - 1] == '2':
            dp[i] = 1 if i == 1 else dp[i - 2]
        else:  # 否则，像 30、00 这种都是属于无效的，没有解法，直接返回0
            return 0
    else:
        dp[i] = dp[i - 1]  # 其他情况的时候，dp[i] 至少有一种解法是通过dp[i - 1] 走途径第i个数字到达
        if '10' < s[i - 1: i + 1] <= '26':  # 如果第i-1 和第 1 个数字组成的两位数是不大于 26的，那么还有另外一种解法是从第i-2个数字途径一个两位数到达
            dp[i] += 1 if i == 1 else dp[i - 2]
return dp[-1]
```

```python
"""
方案2，记忆化缓存
因为用到的之前记录只有第 i-1 个和第 i-2 个，所以可以用类似于斐波拉切数列类似的缓存来处理
时间复杂度：O(n)
空间复杂度：O(1)
"""

if not s or s[0] == '0':
    return 0

prev, curr = 1, 1  # i - 2 和 i - 1 分别都为1
for i in range(1, len(s)):
    if s[i] == '0':
        if s[i - 1] in ['1', '2']:  # dp[i] = dp[i - 2]
            prev, curr = curr, prev
        else:
            return 0
    else:
        if '10' < s[i - 1: i + 1] <= '26':
            prev, curr = curr, prev + curr
        else:
            prev = curr

return curr
```