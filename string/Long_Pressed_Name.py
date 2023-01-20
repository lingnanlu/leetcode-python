'''
按照题意来就行了.
从左到右遍历name, 看typed中是否有这个字符.

这题还是有点意思的, 一开始自己忘记了判断j == len(typed)
这题还有有点难度, 得想好

其实这里是根据name遍历typed.
其实我看也可以根据typed遍历name.
'''


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        # 单独处理一下, 为了以下的不变式写的更方便

        if name[0] != typed[0]:
            return False
        # 分别用来遍历name和typed [0, i)这间的在字母出现在[0, j)之间
        # i, j是下一个要检查的字符.
        i, j = 1, 1

        while i != len(name):
            # 下一个要在typed中找的字符
            c = name[i]

            # 在typed中找c, 跳过和前一个字符相同的
            while j != len(typed) and typed[j] != c:
                if typed[j] == typed[j - 1]:  # 说明重复了,跳过重复的字符
                    j += 1
                else:
                    return False

            # 此时 j == len(typed) 或 typed[j] == c 或 typed[j] != typed[j - 1]
            if j == len(typed):
                # 找不到
                return False
            else:
                i += 1
                j += 1

        # 此时name遍历完了, 但可能typed还有字符.
        while j != len(typed) and typed[j] == typed[j - 1]:
            j += 1

        if j == len(typed):
            return True
        else:
            return False
