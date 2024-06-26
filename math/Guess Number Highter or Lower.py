# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        # m是要猜测范围的[left, right]中间的数，如果n为奇数就是最中间的，如果n为偶数就是n / 2
        # 每次猜测之后，会排除包括n以及n左边或右边的所有数，即尽可能排除更多，保留更少
        # 通过距离来看，比如 3，4这种，不会出现计算之后越界的问题
        left = 1
        right = n
        middle = int((left + right) / 2)
        result = guess(middle)
        while result != 0:
            if result == -1:
                right = middle - 1
            else:
                left = middle + 1
            middle = int((left + right) / 2)
            result = guess(middle)
        else:
            return middle