
'''
试着用底层的和抽象的方式都写一遍

方法一:
底层的, 遍历一遍, 记录下
'''
class First:
    def maxPower(self, s: str) -> int:

        # [0, i)是已经处理的, i指向下一个要处理的
        i = 1

        # 是[0, i)之间已找到的最长的
        maxPower = 1

        # i之前的, 上一个连续字符串的长度
        prePower = 1

        # 注意在循环中要保持不变式为真
        while i != len(s):
            if s[i] == s[i - 1]:
                i += 1
                prePower += 1
                # 这里不要忘记了, 因为忘记了, maxPower是[0, i)之间已找到的最长的
                maxPower = max(prePower, maxPower)
            else:
                i += 1
                prePower = 1
                # 找到一个新的字符
                maxPower = max(prePower, maxPower)

        return maxPower


'''
方法二:
方法一中两个分支有一些共同的部分, 启发我把共同部分提出来, 并做解释
'''
class Second:
    def maxPower(self, s: str) -> int:

        # [0, i)是已经处理的, i指向下一个要处理的
        i = 1

        # 是[0, i)之间已找到的最长的
        maxPower = 1

        # i之前的, 上一个连续字符串的长度
        prePower = 1

        # 注意在循环中要保持不变式为真
        while i != len(s):
            if s[i] == s[i - 1]:
                prePower += 1
            else:
                prePower = 1

            # 此时prePower是[0, i]之间的了, 所以要更新i
            i += 1
            # 此时prePower是[0, i)之间的了. 下一个要更新maxPower
            maxPower = max(maxPower, prePower)

        return maxPower

'''
方法三:
也可以使用两个指针,断言, [i, j)之间的字符相同
'''
class Third:
    def maxPower(self, s: str) -> int:
        # [i, j)之间的字符相同
        i, j = 0, 1

        # 目前找到的最大的
        maxPower = 1


        # 每一次都让i, j指向一个连续的相同的子字符串
        while i != len(s):
            while j != len(s) and s[j] == s[j - 1]:
                j += 1

            # 此时, i, j之间的字符相同
            maxPower = max(maxPower, j - i)

            # 进入下一轮
            i = j
            j = i + 1

        return maxPower

