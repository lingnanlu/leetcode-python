natural_order = "abcdefghijklmnopqrstuvwxyz"

'''
其实就是依次判断两个相邻单词的前后顺序是不是字母表顺序
'''
from typing import List

class First:

    def compare(self, a: str, b: str, order: str):
        # 比较a, b两个单词是否是 a <= b
        k = 0
        while k != min(len(a), len(b)):
            a_k_index = order.find(a[k])
            b_k_index = order.find(b[k])

            if a_k_index < b_k_index:
                return True
            elif a_k_index == b_k_index:
                k += 1
            else:
                return False

        # 此时经过上面的循环比较不出两者大小.
        if a == b:
            return True
        elif len(a) > len(b):
            return False
        else:
            return True

    def isAlienSorted(self, words: List[str], order: str) -> bool:

        # 下一个要比较的两个单词.
        i, j = 0, 1

        while j != len(words):
            a = words[i]
            b = words[j]

            if not self.compare(a, b, order):
                return False

            # 此时, a, b是字典序, 检查后两个
            i = j
            j = j + 1

        # 检查完了, 都是按照字典序的
        return True

'''
方法二
方法一中其实花在定位字符顺序时重复了很多, 可以使用字典优化一下字符查找
'''
class Second:

    def isAlienSorted(self, words: List[str], order: str) -> bool:

        # 下一个要比较的两个单词.
        i, j = 0, 1

        c_2_i = dict()

        for i, c in enumerate(order):
            c_2_i[c] = i

        while j != len(words):
            a = words[i]
            b = words[j]

            if not self.compare(a, b, c_2_i):
                return False

            # 此时, a, b是字典序, 检查后两个
            i = j
            j = j + 1

        # 检查完了, 都是按照字典序的
        return True

    def compare(self, a: str, b: str, order: dict):
        # 比较a, b两个单词是否是 a <= b
        k = 0
        while k != min(len(a), len(b)):
            a_k_index = order[a[k]]
            b_k_index = order[b[k]]

            if a_k_index < b_k_index:
                return True
            elif a_k_index == b_k_index:
                k += 1
            else:
                return False

        # 此时经过上面的循环比较不出两者大小.
        if a == b:
            return True
        elif len(a) > len(b):
            return False
        else:
            return True

'''
方法三:
现有的系统中, 已经实现了比较字符串, 能不能利用上呢?
但这里的顺序不同?
可不可以把word转化成对应自然顺序的字符串, 这样不就可以利用上系统自带的字符串比较功能了?
关键要实现一个翻译功能

这就是利用已知问题的结果
'''
class Third:

    def isAlienSorted(self, words: List[str], order: str) -> bool:

        char_map = {s: t for s, t in zip(order, natural_order)}

        translated = []
        for word in words:
            translated.append("".join([char_map[c] for c in word]))

        i, j = 0, 1
        while j != len(translated):
            if translated[i] > translated[j]:
                return False
            i = j
            j = j + 1

        return True



