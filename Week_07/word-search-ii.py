"""
212. 单词搜索 II
https://leetcode-cn.com/problems/word-search-ii
"""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        构建 Trie:
        {
            'y': {
                'o': {
                    'u': {
                        'WORD': 'you'
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

