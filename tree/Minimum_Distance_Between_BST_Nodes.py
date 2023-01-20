from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
其实就是遍历一遍二叉树, 然后两两计算出相邻结点的差值

方法一:
先转化成数组

方法二:
原地, 不使用额外空间
'''


class First:

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        seq = []
        self.dfs(root, seq)

        minDiff = seq[1] - seq[0]

        for i in range(2, len(seq)):
            minDiff = min(minDiff, seq[i] - seq[i - 1])

        return minDiff

    def dfs(self, node: Optional[TreeNode], seq: List[int]):
        if node is None:
            return
        else:
            self.dfs(node.left, seq)
            seq.append(node.val)
            self.dfs(node.right, seq)


class Second:

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        seq = []

        '''
        python的一种定义函数的方式, 使用这种方式就不用在调用者和被调用者之间传递一些数据用来共享.
        这里的函数可以直接访问包围函数的数据
        方法一中其实是利用一个seq的复制引用来让两者之间交换数据.
        '''

        def dfs(node: Optional[TreeNode]):
            if node is None:
                return
            else:
                dfs(node.left)
                seq.append(node.val)
                dfs(node.right)

        dfs(root)

        minDiff = seq[1] - seq[0]

        for i in range(2, len(seq)):
            minDiff = min(minDiff, seq[i] - seq[i - 1])

        return minDiff


#
'''
原地方法, 需要保持前一个结点的内容.
'''


class Third:

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        # 不变式,
        # 当前要访问结点的前一个结点, None表示当前结点之前没有结点
        # 当前结点和前一个结点之间有差值, -1说明当前结点之前没有结点
        # 好像python不可以直接修改基本类型, 以及引用, 所以使用一个列表传递.
        # 在整个dfs过程中, 一定要保证不变式为真, 这样当遍历完了之后, 由不变式的真就可以得到结果了.
        transfer = [None, -1]

        def dfs(cur: TreeNode):

            if cur is None:
                # 这里直接跳过也是没问题的, 它同样保证了不变式为真
                return
            else:
                dfs(cur.left)
                # 从左边回来之后, 前一个结点才有可能找到
                if transfer[0] is not None:
                    if transfer[1] == -1:
                        transfer[1] = cur.val - transfer[0].val
                    else:
                        transfer[1] = min(transfer[1], cur.val - transfer[0].val)
                # 在进入右边之前, 要保证不变式为真.

                transfer[0] = cur

                dfs(cur.right)


        dfs(root)

        return transfer[1]
