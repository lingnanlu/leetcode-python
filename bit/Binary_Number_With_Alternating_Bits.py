# 其实就是取整数的二进制表示的最低位, 然后一个个的检查
class First:
    def hasAlternatingBits(self, n: int) -> bool:
        # 题目中说n >= 1
        # 先取最低位的数, 作为开始
        prev = n & 1
        n = n >> 1
        # 还有剩余位
        while n != 0:
            # 在有剩余位的情况下, 取一位和之前的比较
            current = n & 1
            # 取一位后, n要记得变化
            n = n >> 1

            # 当前位和前一位相同
            if current == prev:
                return False
            else:
                prev = current

        return True


# 数学方法, 这个真想不到, 利用二进制计算的性质.
class Second:
    def hasAlternatingBits(self, n: int) -> bool:
        a = n ^ (n >> 1)
        return a & (a + 1) == 0
