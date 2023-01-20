
'''
方法一:
模拟题, 按照题意来做.

方法二:
和方法一一样, 就是优化一下代码, 利用python的方式来处理列表
其实就是由一个列表生成另一个列表.

方法三:
既然是列表, 那么O(n^2)的复杂度肯定不接收.
那么, 就想找O(n)复杂度的.
这里的问题就是, 如何快速找到第一个比当前元素小的元素呢? 如果不是使用遍历的话?

其实没什么思路, 我们只好回归到方法一中的, 看看在算法过程中, 有没有重复计算, 能不能省略一些计算.

如[8,4,6,2,3]

对于8, 则遍历4
对于4, 则遍历, 6, 2
此时, 既然遍历了6,2 那么, 我们不想再回过头来遍历6.
其实这里在遍历6, 2过程中, 已经知道2也是比6小, 因为2小于4, 而6 > 4, 所以6 > 2

那么, 这就给了我们希望, 在一遍遍历过程中, 找到比自己小的数.
例一个更复杂一点的例子看看.

[5, 7, 8, 2]
那么, 2, 也就是7, 8之后的.

[5, 7, 6, 2]

6是7之后的最小.

这里我感觉到了遍历的某种规律.

比如当[5, 7, 6, 2]时
我要即要和5比较, 也要和前一个数比较.

比如
5, 7
5, 6, 6, 7
5, 2, 2, 6

这样其实是省略了, 7,2的比较.

[4, 7, 5, 6, 3]

其实最基本的想法就是, 在找第一个元素比当前小的期间, 这中间的元素的最小应该也能确定下来.

这样, 就不会再重复遍历了.
难点就是中间元素的值怎么确定.

现在已知, 中间元素一定比price[i]大, 那么, 还有什么呢?


我感觉, 比较的元素好像就是要和前一个比较, 然后再和开始的比较, 这有点像栈啊. 试试用栈来操作一个.

[4, 7, 5, 6, 3]

[4]

[4, 7]

[4, 5] # 7出栈, 同时把7的最小变成5

[4, 5, 6]

[3] 因为3比4小

大概明白了, 栈内元素是递增的.

入栈元素要和栈顶比, 如果比栈顶要小, 就出栈, 只到出到只剩下空为止.

启示:
这里思路的想出还是从已知算法入手, 寻找哪些计算是可以省略的, 寻找在计算过程中,
还有哪些有用的信息.
以及通过举例子来找规律.

其实这个是什么单调栈的用法. 用栈来保留遍历过程中的额外信息.

'''
class First:
    def finalPrices(self, prices: List[int]) -> List[int]:

        # 表示下一个要产生的商品的折扣
        i = 0
        result = list()

        while i != len(prices):
            # 找到下一个比它价格小的商品
            j = i + 1
            while j != len(prices):
                if prices[j] <= prices[i]:
                    result.append(prices[i] - prices[j])
                    break
                j += 1

            if j == len(prices):
                result.append(prices[i])

            i += 1

        return result


class Second:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        # 一种初始化列表的方式, 表示有n个0
        result = [0] * n
        # 同时得到列表的index和element
        for i, p in enumerate(prices):
            # 计算discount, 注意这里可以先假设一个折扣的默认值
            discount = 0
            for j in range(i + 1, n):
                if prices[j] <= p:
                    discount = prices[j]
                    break

            # 此时算出了折扣
            result[i] = p - discount

        return result

class Third:

    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)

        # 一个栈, 栈里的保存的元素为还没找到其最近小值的元素index
        # 当要出栈时, 就找到其最小值.
        # prices中所有元素都要进栈和出栈一次, 这样就找到所有元素的对应最小值
        stack = []
        stack.append(0)

        # 用于保存对应元素的最近小值
        discounts = [0] * n

        for i in range(1, n):
            # 和栈顶元素对比
            if prices[i] > prices[stack[-1]]:
                stack.append(i)
            else:
                # 把大于等于当前元素的元素全部出栈, 即设置其最近小值.
                while len(stack) != 0 and prices[stack[-1]] >= prices[i]:
                    discounts[stack.pop()] = prices[i]

                # 此时, 栈要不为空, 要不就是栈顶比当前值还小.
                stack.append(i)

        # 此时所有元素都进过栈了, 如果栈中还有元素, 说明没有其最近小值.
        # discounts[i]就是i的最进小值, 也就是折扣值
        return [raw - discount for raw, discount in zip(prices, discounts)]


# 从栈的角度来看, 每个元素入栈一次, 出栈一次, 是两遍遍历.
# 奇怪的是, 算法完全一样, 但使用java就性能快, 不知为什么.
# 正常, 因为力扣上是所有语言在一起比较, 不是python和python比
class Fourth:

    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)

        # 一个栈, 栈里的保存的元素为还没找到其最近小值的元素index
        # 当要出栈时, 就找到其最小值.
        # prices中所有元素都要进栈和出栈一次, 这样就找到所有元素的对应最小值
        stack = []
        stack.append(0)

        # 用于保存最终价格
        finals = prices[0:n]

        for i in range(1, n):

            # 和栈顶元素对比
            if prices[i] > prices[stack[-1]]:
                stack.append(i)
            else:
                # 把大于等于当前元素的元素全部出栈, 即设置其最终价格.
                while len(stack) != 0 and prices[stack[-1]] >= prices[i]:
                    # 要设置的商品的index
                    k = stack.pop()
                    finals[k] = prices[k] - prices[i]

                # 此时, 栈要不为空, 要不就是栈顶比当前值还小.
                stack.append(i)

        # 此时所有元素都进过栈了, 如果栈中还有元素, 说明没有其最近小值.
        # finals[i]就是i的最进小值, 也就是折扣值
        return finals
