"""
874. 模拟行走机器人
机器人在一个无限大小的网格上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令：

-2：向左转 90 度
-1：向右转 90 度
1 <= x <= 9：向前移动 x 个单位长度

在网格上有一些格子被视为障碍物。
第 i 个障碍物位于网格点  (obstacles[i][0], obstacles[i][1])
机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。

返回从原点到机器人所有经过的路径点（坐标为整数）的最大欧式距离的平方。
"""


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dirs = [
            (0, 1),   # 向北
            (1, 0),   # 向东
            (0, -1),  # 向南
            (-1, 0)   # 向西
        ]
        obstacles_set = set()
        for item in obstacles:
            obstacles_set.add(tuple(item))
        i, j = 0, 0
        dir_index = 0
        res = 0
        for com in commands:
            cur_dir = dirs[dir_index]
            if com < -2 or com == 0 or com > 9:
                continue
            if com == -2:
                dir_index -= 1
                dir_index %= 4
                continue
            if com == -1:
                dir_index += 1
                dir_index %= 4
                continue
            # 在当前方向上进行一步步位移 com步
            for k in range(com):
                if (i + cur_dir[0], j + cur_dir[1]) in obstacles_set:
                    break
                i += cur_dir[0]
                j += cur_dir[1]
            res = max(res, i ** 2 + j ** 2)
        return res
