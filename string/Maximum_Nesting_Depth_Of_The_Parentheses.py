'''
这题看着描述一大堆, 其实不是让你判断是否是有效字符串,而是得到最大深度.
这题一看, 你下意识的会想到使用栈之类的, 判断在遍历过程中栈的最大深度.

但我不想这样做, 因为靠下意识的想出思路其实还是以前那种刷题的思维, 刷大量题, 然后靠下意识反应来做题.

你应该把所有的知识忘掉, 然后再想出思路, 这样, 才是真正的会做题了.

方法一:
问题中给出了maxDepth的定义, 是一种嵌套的公式定义, 所以, 我觉得可以实现一种递归的方法

todo

'''
class First:

    # 递归的求一个有效字符串的最大嵌套深度.
    def maxDepth(self, s: str) -> int:

        # depth("") = 0
        if len(s) == 0:
            return 0
        elif len(s) == 1 and s != '(' and s != ')': # depth(C) = 0，其中 C 是单个字符的字符串，且该字符不是 "(" 或者 ")"
            return 1
        else:
            # depth(A + B) = max(depth(A), depth(B))，其中 A 和 B 都是 有效括号字符串
            # 这里要把s分割出两个有效字符串
            s1, s2 = self.divide(s)

            if s2 != '':
                return max(self.maxDepth(s1), self.maxDepth(s2))
            else:
                return self.maxDepth(s[1:-1]) + 1 # depth("(" + A + ")") = 1 + depth(A)，其中 A 是一个 有效括号字符串



    # s是有效字符串, 将s分割成两个字符串. 不能分割出空的.
    def divide(self, s: str) -> (str, str):
        if s[0] != '(':
            return s[0], s[1:]
        else:
            match = list()

            match.append(s[0])

            for i in range(1, len(s)):
                if s[i] == '(':
                    match.append(s[i])
                elif s[i] == ')':
                    match.pop()
                    if len(match) == 0:
                        return s[0:i+1], s[i+1:len(s)]

solution = First()

s = "(1+(2*3)+((8)/4))+1"

print(solution.maxDepth(s))





