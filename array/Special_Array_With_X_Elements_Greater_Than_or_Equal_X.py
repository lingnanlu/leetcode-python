'''
方法一:
最简单的方式, 从0开始试, 直到试到数组最大值, 看看每一个元素是不是特征值
'''


class First:
    def specialArray(self, nums: List[int]) -> int:

        max_element = max(nums)

        for i in range(0, max_element + 1):

            cnt = 0
            for j in nums:
                if j >= i:
                    cnt += 1

            if cnt == i:
                return i
            else:
                return -1

        return -1


'''
方法二:
方法一中, 对于每一个数都要遍历一遍nums, 那么, 能不能减少遍历次数呢? 

因为题目中有大于等于某个数的个数. 而如何能快速知道大于等于某个数的个数呢? 其实可以排个序, 就能以O(1)的复杂度
来得出大于等于某个数的个数.

那么这和结果有什么关系呢? 
有很大关系, 如果知道大于等于某个数的个数a, 这只是从index来说, 再从值上来看是不是真的大于等于这个数的个数是a

其实就是要求
1. 值上满足
2. 顺序上满足

这个思路其实有点技巧, 突破点就是想快速找到大于等于某个数的个数.
'''


class Second:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()

        n = len(nums)
        for i, e in enumerate(nums):

            # x是从位序上来说的大于等于某个数的个数.
            x = n - i

            # 再检查是不是真的值也是这样. 即e >= x且, 前一个数要比x小
            if e >= x and (i == 0 or nums[i - 1] < x):
                return x

        return -1


'''
方法三:
看到值是有限的, 这让人想到能不能对值进行某种统计? 我们使用一个数组来统计某种值出现的次数.
这个, 这个数组的index就是值, 元素就是值的出现次数.

那么, 我们就可以从后往前遍历数组, 找到一个index正好和元素的累加相同的值.

这个思路的突破点是, 由已知条件中的有限值出发, 想到统计数组.
也算是一种突破思路.
'''
class Third:
    def specialArray(self, nums: List[int]) -> int:
        cnt = [0] * 1001

        # 统计次数
        for n in nums:
            cnt[n] += 1

        # 累加比要遍历的值还要大于等于的值的个数.
        accu = 0

        for i in range(1000, -1, -1):
            accu += cnt[i]
            if i == accu:
                return i

        return -1
