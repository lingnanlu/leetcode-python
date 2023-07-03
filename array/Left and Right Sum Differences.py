'''
这题没什么可说的, 就是先求出leftSum和rightSum

这题也可以在空间上优化一下, 因为每次只需要leftSum[i]和rightSum[i], 不需要历史值, 所以空间可以优化为O(1)
'''
from types import List
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        leftSum = [0] * len(nums)

        # i表示要求的leftSum中下一个元素的index
        # accumate表示nums中i左边的元素累积和
        accumate = 0
        i = 0
        while i != len(nums):
            leftSum[i] = accumate
            accumate += nums[i]
            i += 1

        rightSum = [0] * len(nums)

        accumate = 0
        i = len(nums) - 1

        while i >= 0:
            rightSum[i] = accumate
            accumate += nums[i]
            i -= 1

        answer = [0] * len(nums)

        while i != len(answer):
            answer[i] = abs(leftSum[i] - rightSum[i])
            i += 1

        return answer