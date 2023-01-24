'''

方法一:
这题要求原地.
如果是从前往后的话, 会覆盖一些原来的值.这肯定不行.

那么, 从后往前呢? 比如

arr = [1,0,2,3,0,4,5,0]

对于3,
1. 你不知道每个数要平移几位. 怎么办?
2. 还有不知道从哪一位开始截断.

其实对于第2个问题, 可以通过遍历一遍, 计算个数知道最后到哪里会结束.
对于第一个问题, 其实和解决第2个问题过程中的找到的0的个数有关.

方法二:
方法一有些复杂, 要仔细思考不变式以及各种变量含义, 不过幸好, 自己是一遍过
那么, 能不能有其它方法呢?
我们做过的就是将每一个元素平移一位那种.
能不能利用已经做过的题的方法?

现在问题是有多个0, 导致后面的数不知道要平衡几位.
我们能不能忽略多余的0, 然后就考虑第一个, 然后平移一位?

'''
from typing import List

class First:

    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # 利用i遍历一遍数组, 边遍历边计算出重复0后的元素个数, 放入count中
        # zero_count用于计数这个过程中出现的0
        i = 0
        zero_count = 0
        count = 0

        while i != len(arr):
            if arr[i] == 0:
                count += 2
                zero_count += 1
            else:
                count += 1

            i += 1
            if count >= len(arr):
                break

        # 此时 count 为将[0, i)之间的数复制0之后的个数
        # count == len(arr) or count == len(arr) + 1
        # zero_count 为[0, i)之间的0的个数.
        # [0, i)为最终要保留的数.
        # 还容易知道, 如果len(arr) == count 那么, arr[i - 1] != 0
        # 如果len(arr) + 1 == count 那么,arr[i - 1] == 0

        # 下面就是根据上面的值来对[0, i)之间的数进行平移了.

        # 依次移动[i - 1, 0]之间的数
        # zero_count 就是偏移量
        for j in range(i - 1, -1, -1):
            if arr[j] == 0:
                arr[j + zero_count - 1] = arr[j]
                # 复制最后一个0时, 注意会不会越界
                if j + zero_count - 1 + 1 < len(arr):
                    # 不越界就复制一个0
                    arr[j + zero_count] = 0
                zero_count -= 1  # 更新偏移量
            else:
                arr[j + zero_count] = arr[j]

class Second:

    def duplicateZeros(self, arr: List[int]) -> None:




