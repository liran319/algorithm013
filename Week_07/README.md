# 单词搜索II

#### 思考和试错
> 这一题前后纠正写法花了两天时间，主要原因在构建Trie的时候结构有些混乱，比如记混了以为 `WORD` 结束标记是在字典树的叶子节点的字典里，```[['a', 'a'],['a', 'b']]```就会一直少一个 `aaab` 的结果；
> 后来参考了老师的 defaultDict 以及网友的 setDefault的写法，直接将 Trie 结构简化成纯粹的键值树（如下），并且在每一个 word 的尾字母的hashmap里添加 `”WORD": word`的键值，用于提示成功获取一个单词；

#### 复杂度分析
* 假设 board 长宽分别为 m, n;
* K, N, L 分别代表 words 的个数，每一个 word 的平均长度，word的最大长度

1. 构建 Trie: O(KN)
2. 最外层遍历 board: O(mn)
3. 递归遍历每一个 board 中的字母的时候，以为都会向上下左右4个方向扩散，又因为本层遍历之前已经有把来源坐标的字母标记为 ’#‘了，所以最多会继续遍历剩下3个方向L - 1 次：O(4*3^(L-1))

时间复杂度 O(KN + mn*4*3^(L-1)) ≈ O(mn*4*3^(L-1))， 因为 KN相对于递归的时间复杂（指数级）可以忽略；
空间复杂度：O(KN), 主要的 空间复杂度在于构建 Trie

```python
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        构建 Trie:
        {
            'y': {
                'o': {
                    'u': {
                        'WORD': 'you'
                        'r': {
                          'WORD': 'your'
                        }
                    }
                },
                'e': {
                    's': {
                        'WORD': 'yes'
                    }
                }
            }
        }
        """
        if not len(board) or not len(board[0]):
            return []
        res, m, n = set(), len(board), len(board[0])

        trie = {}
        for word in words:
            node = trie
            for letter in word:
                if letter not in node:
                    node[letter] = {}
                node = node[letter]
            node['WORD'] = word

        def dfs(curr, i, j):
            tmp = board[i][j]  # 缓存当前字母
            curr = curr[tmp]   # 更新当前字典
            if 'WORD' in curr:  # 因为构建 trie 的时候，单词结束字符是在最后一个字母的字典里，所以要判断新的curr
                res.add(curr['WORD'])
                # 注意，此处不能直接return， 因为要考虑到还有路径重叠的单词，比如 'aaa' 和 'aaab'
            board[i][j] = '#'
            for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = i + dx, j + dy
                if x < 0 or x >= m or y < 0 or y >= n or \
                    board[x][y] == '#' or board[x][y] not in curr:
                    # 剪枝
                    continue
                dfs(curr, x, y)
            board[i][j] = tmp


        root = trie
        for i in range(m):
            for j in range(n):
                if board[i][j] in root:
                    dfs(root, i, j)
        return list(res)
```

# 并查集（朋友圈）
> 一般用于【判断有多少个朋友圈（集合）】、【a和b是不是朋友】、【x属于哪个集合】等等

## 理解的困难点

因为并查集也看了两天多，因为一开始看有些太抽象了，基本原理看明白了，就是具体做题的时候有一步, 一直没理解：`p = [i for i in range(n)]`，再后来看了网友的总结有了理解，这一步是为了先初始化 n 个元素各自的集合，即初始状态是各自为单独的集合 p[i] == i， 然后根据矩阵关系来判断和合并同一个集合，最后求得所有合并任务完成后的所有集合的个数。（实在是秒哇...)

# 高级搜索

* 剪枝：在遍历状态树的时候，提前判断当前这一步是不是`可行或最优`且`不和之前的路径重复`，如果不满足，则跳过这一条路就，即为”剪枝“；
  > 在前面的`朋友圈`问题使用并查集来做题的时候，因为考虑到对称性，只需要遍历一半的矩阵，把对称的部分跳过，也就是剪枝的理念；
* 双向BFS：对于双向联通的图或者树形结构，可以从起点和终点分别向下向上搜索，一旦在中间某一步匹配到了，则最短路径就找到了；
* 启发式搜索（优先级搜索、A*搜索）：在搜索过程中，根据某个规则设定优先级，在备选的节点中找优先级高的节点，进行树或图的搜索

## 双向BFS模板

```python

start_queue, end_queue, visited, setps = [start], [end], set(), 0
visited.add(start_queue)

while start_queue and end_queue:
    if len(start_queue) > len(end_queue):  # 比较 start_queue 和 end_queue, 使得 start_queue 始终为两者中的较短这样，这样可以减少遍历的次数
        start_queue, end_queue = end_queue, start_end

    for i in range(len(start_queue)):
        curr = start_queue.pop(0)

        for child in curr.children:
            if child in end_queue:
                return steps + 1
            if child in visited:
                continue
            visited.add(child)
            start_queue.append(child)
        steps += 1
    return 0
```

# AVL 和 红黑树

## AVL
* 是一个高度自平衡的二叉搜索树；
* 每个节点都会保存他自己的平衡因子：每一个节点的右子树的高度减去左子树的高度；
* 四种旋转操作：
  1. 左左子树 ——> `右旋`；
  2. 右右子树 ——> `左旋`；
  3. 左右子树 ——> `左右旋`；
  4. 右左子树 ——> `右左旋`；
* 不足：
  1. 节点需要额外空间存储平衡因子；
  2. 会频繁修改，维护成本高


## 红黑树
* 金丝平衡二叉搜索树；
* 任意一个节点的左右子树高度差`小于2倍`;

特点:
1. 每个节点要么是红色，要么是黑色；
2. 根节点是`黑色`；
3. 每个叶子结点是`黑色`;
4. 不能有相邻接的两个红节点；
5. 从`任意一个节点`到`其每一个叶子结点`都包含`相同数目的黑色节点`；

## 对比

|          | AVL                                             | 红黑树                                                    |
| -------- | ----------------------------------------------- | -------------------------------------------------------- |
| 查询    | AVL更快，因为高度平衡，查找次数等于树的最大深度         | 树的左右子树差会在0~2倍之间，查询次数会多                       |
| 添加删除 | AVL旋转更多，要维护高度平衡，平衡因子要保证            | 红黑树更快，因为高度差容错高，高度差小于两倍可以不用旋转           |
| 存储空间 | AVL需要平衡因子（INT型)                            | 红黑树主需要一个bit(0 or 1)的空间来存储颜色                    |
| 使用场景 | 读取操作非常多的时候                                | 插入编辑操作略多的时候                                       |