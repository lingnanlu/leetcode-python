'''
这题肯定不能直接与翻转所有子数组,因为你不知道要翻转哪个, 翻转多少次.

所以, 得转换成一个等价的题目.

那么, 如何判断一个数组能变成另一个呢?

其实就是将target 从左到右遍历.

对于target中的每一个数, 看arr中是不是有另一个数与之对应, 如果是, 就可以翻转过来.

如果每次只能翻转两个, 其实就是冒泡排序

其实就是判断两个数组中的数是不是相同.

方法一:
排序后, 比较是否相同

方法二:
因为值空间有限, 所以可以统计值的数量
'''
from typing import List, Counter


class First:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()

        return target == arr

class Second:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # 别忘记了一种方便的统计各个元素数量的快捷方式
        return Counter(target) == Counter(arr)
