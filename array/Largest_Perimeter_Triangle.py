'''
方法一:
其实就是找所有三角形, 然后找最大. 暴力方法.
'''
class First:
    def largestPerimeter(self, nums: List[int]) -> int:

        ans = float("-inf")

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if self.foobar(nums[i], nums[j], nums[k]):
                        ans = max(ans, nums[i] + nums[j] + nums[k])

        if ans == float("-inf"):
            return 0
        else:
            return ans

    def foobar(self, a: int, b: int, c: int) -> bool:
        return (a + b) > c and (a + c) > b and (b + c) > a

'''
方法二:
既然要找最大周长, 那么三边越长越好, 越大越好
这让人想起, 先排序试试?

现在就是要找三个值, 要求

1. 尽可能大
2. 能组成3角形

那么, 怎么找呢? 自然想到的就是先看最大的三个, 如果能组成, 那么就是它了, 如果不能呢?
下一个三个是哪些呢? 想一想, 其实就是往前移动一下, 排除最大那个, 往前找三个就行.
'''
class Second:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        # i, j, k分别指向倒数第三, 第二, 第一个
        i, j, k = -3, -2, -1

        while i >= -len(nums):
            if (nums[i] + nums[j]) > nums[k]:
                return nums[i] + nums[j] + nums[k]
            else:
                # 这三个组不成三角型
                i -= 1
                j -= 1
                k -= 1

        # 此时没有能组成三角形的
        return 0

# 方法二的另一种写法, 习惯使用range
class Third:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums) - 1, 1, -1):
            if nums[i - 2] + nums[i - 1] > nums[i]:
                return nums[i - 2] + nums[i - 1] + nums[i]

        return 0