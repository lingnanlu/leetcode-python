# 其实就是统计text中balloon中处个字符的个数
from collections import Counter


class First:
    def maxNumberOfBalloons(self, text: str) -> int:
        # 注意这里的初始化的方式, 其实python初始化这种很方便.
        cnt = {'a': 0, 'b': 0, 'l': 0, 'o':0, 'n':0}

        # 1. 先统计各字母字符数
        for c in text:
            if c in 'balon':
                cnt[c] += 1

        cnt['l'] //= 2
        cnt['o'] //= 2

        # 2. 找数量最少的
        least = cnt['a']
        for v in cnt.values():
            least = min(least, v)

        return least

# 一种更简洁的写法, 使用python的Counter和语法糖
class Second:
    def maxNumberOfBalloons(self, text: str) -> int:

        # 从text中得到一个只有balon的序列,然后从这个序列中做一个统计
        cnt = Counter(ch for ch in text if ch in 'balon')

        cnt['l'] //= 2
        cnt['o'] //= 2

        return min(cnt.values()) if len(cnt) == 5 else 0
