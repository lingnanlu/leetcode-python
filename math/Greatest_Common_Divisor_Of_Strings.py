import math

'''
这题理解其实简单, 但找起来就难多了, 如何找最大呢? 
一个一个试? 好像不行.

那怎么办? 
一想到最大公约数, 我们能想到求两个数字的最大公约数, 但这里是字符串啊?

数字在哪? 其实字符串的长度就是数字.

那么, 我们就可以先找两个字符串长度的最大公约数, 先尝试这个长度的字符串是不是可以组成str1和str2

如果不能呢? 要尝试一个更小的长度. 这个长度是多少呢? 原来的 -1么? 肯定不行, 这样不能保证能整除.

假设x是最大公约数, 则 

a / x, b / x能整除.

下一个公约数是多少呢? 我猜应该是

a / x / y, b / x/ y

这个应该要证明, 但这里我证明不了, 先假设是这样的, 试一试吧.

注:
这题其实不好做, 因为好的解法对数学证明要求高, 所以不是一个好题. 太偏重数学证明了.

'''
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        a = len(str1)
        b = len(str2)
        # 第一个公约数
        gcd = math.gcd(a, b)

        while gcd != 1:
            # 验证其是否是字符串的最多公约数
            common = str1[0:gcd] # 猜测的相同的部分

            if common * (len(str1) // gcd) == str1 and common * (len(str2) // gcd) == str2:
                return common
            else:
                # 尝试下一个.
                a //= gcd
                b //= gcd
                gcd = math.gcd(a, b)

        # 此时gcd为1, 再验证一次
        common = str1[0:1]
        if common * len(str1) == str1 and common * len(str2) == str2:
            return common

        # 此时没有最大的
        return ""

