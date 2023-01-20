'''
这题猛一看, 好像似乎挺难.
但其实试着从左到右翻译, 其实也不难.
其实你担心的问题就是要看几位呢? 可能看一位也行, 看两位也行? 那不是每走一位. 就有两种情况吗?
这样会不会情况很多?
其实不是的, 这里每往前看一步, 其实就一种情况. 所以其实很简单.
为什么就一种情况呢? 因为可以根据是0还是1来判断.

就一直解码, 直到只剩下一个字符, 且是0
'''
class Solution:

    def isOneBitCharacter(self, bits: List[int]) -> bool:

        i = 0

        # i不断移动, 当跳出循环时, i >= len(bits) - 1, 说明还剩最多1个字符.
        while i < (len(bits) - 1):
            if bits[i] == 0:
                i += 1
            else:
                i += 2

        if i >= len(bits):
            return False
        else:
            # 还剩一位
            return bits[i] == 0





