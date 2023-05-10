"""
这题其实就是一个模拟题,题目中已经给出了解答步骤.
关键就是准确的用代码表达出来

大概描述如下
1. 从前向后一个一个字符进行查看.
2. 如果当前处于竖线对之中, 就跳过
3. 如果不处于竖线对之中, 就统计*的个数.

"""
class Solution:
    def countAsterisks(self, s: str) -> int:

        # 一开始就是处于竖线对之外的.
        out = True
        count = 0
        for c in s:
            if c == '|':
                out = not out
            elif out:
               if c == '*':
                   count += 1

        return count

