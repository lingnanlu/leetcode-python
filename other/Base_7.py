# 考察进制转化

class Solution:
    def convertToBase7(self, num : int) -> str:

        if num == 0:
            return "0"

        # 不考虑符号
        remain = abs(num)

        # ans中是每一位的字符串形式
        ans = []
        while remain != 0:
            ans.append(str(remain % 7))
            remain = int(remain / 7)

        if num < 0:
            ans.append("-")

        return "".join(reversed(ans))
