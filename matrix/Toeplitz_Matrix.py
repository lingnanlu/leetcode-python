'''
方法一:

考察二维矩阵的斜对角线的遍历方式.
这个就是找一下i, j的变化规律.

啊哈!灵机一动
其实这个题的关键点就是在于模仿二维遍历的过程, 如何移动到下一个点, 如何确认终点等等.
这个代码看起来复杂, 其实只要照着模仿二维的做, 就能一次正确

方法二:

题目要求, 每次只能读一行, 所以, 大概思路就是
1. 读一行, 记录一些信息
2. 再读新的一行
3. 判断新的一行和前面的一行是不是一样的.

这就要观察相邻两行的特点. 很容易发现, 相邻两行的不同就是将第一行右移一位就和下一行一样了.
'''
class First:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        # 可以看成二维遍历的第一维, i的变化其实是第一行从最后一列到第一列
        # 到达第一列之后, 从第一行到最后一行, 终点是 (len(matrix), 0)
        i = (0, n - 1)

        while i != (m, 0):
            # j 可以看成二维遍历的第二维
            i_e = matrix[i[0]][i[1]]
            j = i
            while j[0] != m and j[1] != n:
                j_e = matrix[j[0]][j[1]]
                if j_e != i_e:
                    return False
                else:
                    # j移动到下一个
                    j = (j[0] + 1, j[1] + 1)

            # i 移动到下一个.
            if i[1] != 0:
                # 往前移动
                i = (i[0], i[1] - 1)
            else:
                # 往下移动
                i = (i[0] + 1, i[1])

        return True

'''

'''
class Second:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        # 要读的行
        i = 0

        # 指向前一行
        pre = None

        # 还有要读的行
        while i != m:
            # 读一行
            row = matrix[i]

            if pre == None:
                pre = row
                i += 1
            else:
                # 将row右移一位, 然后和pre比较, 其实不用真正的右移, 错位比较就好.
                if row[1:] != pre[0:n - 1]:
                    return False
                else:
                    i += 1

        return True






