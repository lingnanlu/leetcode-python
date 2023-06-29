'''
一个类似的问题是, 给定一个数组, 判断是否有两个整数相同.
方法就是统计出现的次数.
而这里要求和这个有些不同, 但可以转化成判断两个整数是否相同.

注意defaultdict的使用方式, 这是一个自带初始化的字典. 用起来比较方便.
'''

from typing import List
from collections import defaultdict
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        count = defaultdict(int)

        for i in range(len(nums) - 1):
            k = nums[i] + nums[i + 1]
            count[k] += 1
            if count[k] == 2:
                return True
            
        return False
        
