'''
方法一:
就是不断累加, 模拟的方式.

方法二:
这种有规律的数字, 一般可以使用数学的方式

第一周是 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28
第二周是 28 + 7 = 35
第三周是 35 + 7 = 42

其实是一个等差数列

'''
class First:
    def totalMoney(self, n: int) -> int:

        ans = 0

        # 上一个周一存入的钱, 因为还没存入过, 所以可以为0
        last_monday = 0

        # 用于保存第i天要存入的钱, 这个0是一个占位
        money = 0
        for i in range(1, n + 1):
            # 又到了一个新的周一
            if i % 7 == 1:
                last_monday += 1
                money = last_monday
            else:
                money += 1

            # 存入钱
            ans += money

        return ans

class Second:
    def totalMoney(self, n: int) -> int:

        # 求一共几周
        week = n // 7

        ans = 28 * week + (week * (week - 1) * 7) // 2

        # 还剩几天
        remain_days = n % 7

        if remain_days != 0:
            # 周一要存入的
            start = week + 1
            for i in range(1, remain_days + 1):
                ans += start
                start += 1


        return ans

