from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
这题应该是DFS遍历, 但有三个值

1. 子树之和
2. 该结点坡度
3. 整个数的坡度
'''
class First:

    def findTilt(self, root: Optional[TreeNode]) -> int:

        # 整个数的坡度, 等于每个结点坡度之和
        # 不能传整型, 只能转一个一元素的容器
        tot = [0]

        # dfs整个树, 返回值为左边的树的结点之和
        def dfs(node: TreeNode) -> int:

            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            tot[0] += abs(left - right)

            return left + right + node.val

        dfs(root)

        return tot[0]

# 和方法一一样, 就是利用成员变量
class Second:

    def __init__(self):
        # 一个成员变量, 类似方法一中的tot=[0]
        self.ans = 0

    def findTilt(self, root: Optional[TreeNode]) -> int:

        self.dfs(root)

        return self.ans

    def dfs(self, node: TreeNode) -> int:
        if node is None:
            return 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        self.ans += abs(left - right)

        return left + right + node.val