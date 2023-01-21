
'''
这题没什么难的, 认真一点, 其实就是关键两点

1. 依次取低位
2. 保存结果.
'''
class First:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ans = []

        # 分别指向num的最低位, 将要取的值.
        i = len(num) - 1

        # 进位
        carry = 0

        # num和k还有位可以取
        while i >= 0 and k != 0:
            # 取num
            a = num[i]
            i = i - 1
            # 取k
            b = k % 10
            k = k // 10

            ans.append((a + b + carry) % 10)
            carry = (a + b + carry) // 10

        # 看看num和k中谁还有剩余
        # i还有剩余
        while i >= 0:
            a = num[i]
            i = i - 1
            ans.append((a + carry) % 10)
            carry = (a + carry) // 10

        while k != 0:
            a = k % 10
            k = k // 10
            ans.append((a + carry) % 10)
            carry = (a + carry) // 10

        # 最后看下carry
        if carry == 1:
            ans.append(carry)

        return ans[::-1]




