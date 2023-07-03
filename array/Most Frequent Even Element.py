'''
又是一个最xx的问题, 一个类似的问题就是最大数.
这里的最要求是频率最多, 所以要先统计频率
而且是偶数, 这就要过滤
而且要最小, 所以当频率一样时, 要选择最小
'''
from types import List
from collections import Counter

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count = Counter(nums)

        # 1表示还没找到
        result = 1
        for key, value in count.items():
            if key % 2 == 0:
                if result == 1:
                    result = key
                else:
                    if value > count[result]:
                        result = key
                    elif value == count[result]:
                        result = min(result, key)
        
        if result == 1:
            return -1
        else:
            return result
            
