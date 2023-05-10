# 最直观的, 就是试, 从小到大, 一个一个的尝试. 然后统计满足要求的.
# 这里的关键就是尝试的范围, 要有一个上界
class First:
    def commonFactors(self, a: int, b: int) -> int:
        count = 0

        for i in range(1, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                count += 1

        return count

# 方法一的关键就是循环的次数, 我们可以进一步想办法
# 减少
# 比如对于 32 = 2 * 16, 当能被2整除时, 其实也能被16整除
# 此时就有两个因子.
# 现在要找两个数的公因子, 我们简化一下问题, 只找一个数的因子.
# 两个数的公因子就是两个数的因子集合的交集.
# 
from math import sqrt, floor
class Second:
    def commonFactors(self, a: int, b: int) -> int:
        return 0
    
# 枚举到最大公约数
# 这是一个技巧, 知则知, 不知则不知, 所以不要在意
# 最关键的就是你能从第一个方法中, 找到优化的思路
# 即想办法减少枚举的数的个数.
class Third:

