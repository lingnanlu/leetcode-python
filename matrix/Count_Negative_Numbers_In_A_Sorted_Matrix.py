'''

方法一:
最简单的方式, 遍历一遍, 统计负数

方法二:
在每一行找负数时, 可以利用二分查找来找, 这样会性能好一些

方法三:
给出提示了, 要求O(m + n), 然后题目给出了有序的条件.
想到如何利用有序来达到O(m + n)

从左上角开始不行
试试右上角开始吧

启示:
本题的方法三是自己看的答案, 并没有想出来.
我觉得问题在于, 二维图像在脑子里不够直观, 应该画个图, 可能就把这个问题解决了.

'''
from typing import List


class Third:
    def countNegatives(self, grid: List[List[int]]) -> int:
        i, j = 0, len(grid[0]) - 1
        result = 0
        # 左下角是终止.
        while i != len(grid) and j >= 0:
            if grid[i][j] < 0:
                # 由这个点以下的元素都是负数
                result += len(grid) - i

                # 向左走
                j -= 1
            else: # 此时这个点是正的, 所以往左走不行了, 往下走
                i += 1

        return result
