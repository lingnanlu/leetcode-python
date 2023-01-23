'''
方法一:
关键就是得到一个数的位数

方法二:
我们知道如何找到一个字符串中字符个数, 要是每个整数是字符串就好了, 所以先变化成字符串

方法三:
利用以10为底的对数, 学会使用以10为底的对数
'''
from typing import List


class First:
    def findNumbers(self, nums: List[int]) -> int:
        return len([n for n in nums if self.digit(n) % 2 == 0])

    def digit(self, num: int) -> int:

        # 0做特殊处理
        if num == 0: return 1

        ans = 0
        while num != 0:
            # 每右移一位, ans + 1
            num //= 10
            ans += 1

        return ans

class Second:
    def findNumbers(self, nums: List[int]) -> int:
        str_num = [str(n) for n in nums]

        return len([n for n in str_num if len(n) % 2 == 0])

class Third:
    def findNumbers(self, nums: List[int]) -> int:
       return sum(1 for n in nums if int(math.log10(n) + 1) % 2 == 0)
