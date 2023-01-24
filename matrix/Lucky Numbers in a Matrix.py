'''
方法一:
就按照题意来, 对于每一个数, 判断是不是幸运数, 那么时间复杂度会是

O(m*n(m + n))

方法二:
方法一中的要判断的candidate太多了. 可不可以缩短一点.

你看, 这里要限制条件是两个, 我们可以先只满足一个条件, 把候选集缩小到m, 然后再满足第二个条件.

1. 先找各行最小的
2. 然后判断其是不是所在列最大的.

时间复杂度 O(m * n) + O(m * n)  每一步都是O(m * n)

灵机一动:

方法二其实就是看题目要找满足两个条件的数, 其实可以先找满足一个条件的, 这样一方面好找, 另一方面缩小candidates的数量.

方法三:

方法一中, 对于每一个数都要判断一次是不是行最小和最大, 这个m +n其实重复了, 我们可以先把第一行的行最小和列最大一次性计算出来
这样就不用对于第一个元素都计算了.
'''
from typing import List


class Second:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        ans = []

        # 先找同一行中最小的元素, 记录其值和列坐标.
        row_min = []
        for row in matrix:
            v = min(row)
            i = row.index(v)
            row_min.append((v, i))

        # 对每一个行最小的, 判断其是不是所在列最大的.
        for v, col in row_min:

            # 找所属列最大的
            max_e = matrix[0][col]
            for i in range(0, len(matrix)):
                max_e = max(max_e, matrix[i][col])

            # 满足了第二个条件
            if v == max_e:
                ans.append(v)

        return ans

class Third:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minRow = [min(row) for row in matrix]
        minCol =



