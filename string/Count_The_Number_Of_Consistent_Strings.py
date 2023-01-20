'''
方法一:
模拟题, 就是按个判断words中的字符串的字母是不是在allowd中.
这个判断其实可以优化一下.

启示:
表示某些东西存在与否, 可以使用
1. 集合
2. 数组中的true和false
3. 位 0, 1
'''
from typing import List


# 利用数组
class First:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        charExist = [False] * 26

        for c in allowed:
            charExist[ord(c) - ord('a')] = True

        count = 0

        for word in words:
            # 表示目前已迭代的word的字符, 都在allowed中 (因为没有迭代字符, 所以为true有意义)
            match = True
            for c in word:
                if not charExist[ord(c) - ord('a')]:
                    match = False
                    break

            if match:
                count = count + 1

        return count


# 利用集合
class Second:

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        sset = set([c for c in allowed])

        count = 0

        for word in words:
            # 表示目前已迭代的word的字符, 都在allowed中 (因为没有迭代字符, 所以为true有意义)
            match = True
            for c in word:
                if c not in sset:
                    match = False
                    break

            count += 1 if match else 0

        return count


# 利用一个32位int表示某字符是不是在其中
class Second:

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        mask = 0

        for c in allowed:
            mask |= 1 << (ord(c) - ord('a'))

        count = 0

        for word in words:
            # 表示目前已迭代的word的字符, 都在allowed中 (因为没有迭代字符, 所以为true有意义)
            match = True
            for c in word:
                if not (mask >> (ord(c) - ord('a'))) & 1:
                    match = False
                    break

            count += 1 if match else 0

        return count
