'''
方法一:
要求的是这样一个数组
1. 每一个元素不相同
2. 该元素至少在两个数组中出现过.

直接找, 行不行?
我觉得行, 每一个元素不相同, 可以利用集合.
而一共就3个数组, 所以, 两两组合也可以穷举出来
所以, 两两找共同的元素就行.

这里最复杂的应该是两两找共同元素, 有如下几个方法
1. 两个当成集合, 求交集: 这是利用库函数, 不知道时间复杂度
2. 遍历其中的一个, 在另一个中找有没有存在的, 这种最差就是O(n^2)

这样不行, 那么, 还有没有更简单, 直观的方法呢?
求两个数组中共同出现的元素数, 它和不是共同出现的有什么区别呢?
共同出现就是出现了两次

对于三个数组其实是一样的, 我们可以统计次数.

而对于每个值有一个1 <= 100的范围, 所以, 不需要使用hash了.


方法二:

方法一中要使用三个数组来标记, count[i]表示在某个数组中存不存在.
那么, 能不能使用count[i]来表示在三个数组中都存在?
想到可以利用位运算.

比如说, 011, 101, 110, 111都算


启示:

一个整数其实可以表达很多的信息, 如果把它当成位的集合的话.
'''
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:

        count1 = [0] * 101
        for v in nums1:
            if count1[v] == 0:
                count1[v] = 1
        
        count2 = [0] * 101

        for v in nums2:
            if count2[v] == 0:
                count2[v] = 1

        count3 = [0] * 101

        for v in nums3:
            if count3[v] == 0:
                count3[v] = 1

        sum = [0] * 101

        for i in range(1, 101):
            sum[i] = count1[i] + count2[i] + count3[i]


        result = []
        for i in range(1, 100):
            if sum[i] >= 2:
                result.append(i)
        
        return result

class Second:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:

        count = [0] * 101

        # 将最低位设置为1
        for v in nums1:
            count[v] = 1

        # 将倒数第二位设置为1
        for v in nums2:
            count[v] = count[v] | 2

        # 将倒数第三位设置为1
        for v in nums3:
            count[v] = count[v] | 4
        
        result = []
        for i, v in enumerate(count):
            if v == 3 or v == 5 or v == 6 or v == 7:
                result.append(i)

        return result

       