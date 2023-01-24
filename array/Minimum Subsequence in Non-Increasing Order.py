'''
方法一:
这题看着好像复杂, 但其要求

1. 尽可能大
2. 尽可能短
3. 不要求连续, 可以是任意顺序.

直观的感觉就是从大到小排下序, 然后取前面的元素.

方法二:
方法一中使用了一个新的数组, 其实没必要, 可以在原数组找到结果后, 利用一个切片就行.
'''
from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)

        total = sum(nums)

        ans = []

        # ans中累加的
        accu = 0
        for n in nums:
            accu += n
            ans.append(n)

            if accu > (total - accu):
                break

        return ans