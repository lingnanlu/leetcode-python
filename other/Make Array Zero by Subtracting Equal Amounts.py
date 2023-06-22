'''
这题的意思就是先选出一个正整数, 然后所有数减去这个正整数, 重复只到所有的数为0

最直观的就是模拟, 就模拟上面所说的操作步骤, 看看经过几步得到答案.

这种方法的关键就是
1. 找出最小的正整数
2. 判断是否全是0

我想找出最小的正整数, 只要是能排除0, 然后剩下的从小到大排序就行.

而且这个排序不需要每次都排.

而判断是否全时0可以通过有没有不是0的元素.

这种方式注意使用循环不变式, 注意边界.

方法二:

方法一有些麻烦, 能不能有更直接的方法, 不是利用模拟的?
举几个例子, 比如说

[1, 1, 1] => [0, 0, 0]

[1, 2, 8] => [0, 1, 7] => [0, 0, 6] => [0, 0, 0]

[3, 5, 7] => [0, 2, 4] => [0, 0, 2] => [0, 0, 0]

[3, 5, 5] => [0, 2, 2] => [0, 0, 0]

发现, 好像有几种整数有关, 有三种说明就是要做几次操作


'''

from typing import List

class First:
    def minimumOperations(self, nums: List[int]) -> int:

        nums.sort()

        lenth = len(nums)

        count = 0

        # last指向上一次非0元素的index, 这里的-1只是一个点位, 说明还没开始找过
        last = -1
    
        while True:
            # 1. 先找第一个非0元素
            # 2. 然后所有的元素减去这个元素.

            # 因为last是上一次非0元素的index, 而上一次操作后last的元素肯定为0, 所以要向后一位开找
            p = last + 1
            while p != lenth and nums[p] == 0:
                p += 1
            
            # 此时要不就是全部为0了, 要不就是找到了
            if p == lenth:
                break
            else:
                count += 1
                last = p
                minInt = nums[p]
                q = p
                while q != lenth:
                    nums[q] -= minInt
                    q += 1

        return count
            

class First:
    def minimumOperations(self, nums: List[int]) -> int:
       return len(set(nums) - {0})