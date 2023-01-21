'''
这题还是要多读两遍才能理解, 不是那么直观.
用自己的话重复一遍吧.

已知
1. s字符串, 长度为n
2. s字符串的字符由I, D两种组成

求
1. 一个长度为n + 1的整数数组
2. 这个数组的元素是[0, n]之间的数字, 每一个出现且仅出现一次

这题的感觉就是, 要遍历s, 在遍历过程中, 生成数组.

那么, 要想生成数组就得知道
1. 首元素是什么
2. 如何由前一个元素生成后一个元素.

仔细想了想, 好像还真不好做, 我怎么知道第一个首元素是多少? 我怎么知道遇到I, D是增加多少还是减少多少?

因为这里有一个要求必须是在[0, n]之内的数, 且不重复.

那么, 我们放开一点要求, 不要求是[0, n]这间的, 但要求不重复, 且是某个连续的. 看看能不能解

首先, 首元素, 我们最先想到是0
然后, 遇到I, 我们就加一, 遇到D, 我们就减一
但又不能使用之前使用过的数.

这样我们就可以得到一个连续序列. 步长是1, 但范围不是[0, n]
但我们可以修正这个范围.

方法二:
方法一试了一下, 结果是正确的, 但性能太差, 我感觉最消耗时间的是判断有没有使用过.
这里可以简化一下. 其实只是要知道过去已使用过的最大的数和最小的数.

啊哈, 灵机一动!
这题的突破点就是大胆试验, 先不考虑所有条件, 先尝试一个最特殊的值, 然后让其满足性质.
方法一证明了正确性, 但性能有些差, 方法二则注意到其实要找比已用过的最大大一, 最小小一.
所以再次优化了一下, 
'''
class First:
    def diStringMatch(self, s: str) -> List[int]:
        ans = [0] * (len(s) + 1)
        i = 1 # i指向ans中下一个空位.
        # 记录已经使用过的数
        already_used = set()

        already_used.add(0)

        for c in s:
            if c == 'I':
                # 要比前面的数要大. 且没使用过
                n = ans[i - 1] + 1
                while n in already_used:
                    n += 1
                ans[i] = n
                already_used.add(n)
                i += 1
            else:
                # 要比前面的数要下, 且没使用过
                n = ans[i - 1] - 1
                while n in already_used:
                    n -= 1
                ans[i] = n
                already_used.add(n)
                i += 1

        # 此时, ans中的都是步长为一个, 需要修正一下.
        shift = min(ans)

        if shift == 0:
            # 正好
            return ans
        elif shift < 0:
            # 每一个元素都要 + abs(shift)
            shift = abs(shift)
            return [e + shift for e in ans]
        else:
            # 每一个元素都要减去shift
            return [e - shift for e in ans]

class Second:
    def diStringMatch(self, s: str) -> List[int]:
        ans = [0] * (len(s) + 1)
        i = 1 # i指向ans中下一个空位.
        # 记录已经使用过的最小的数
        least = 0
        # 记录已经使用过的最大的数
        most = 0

        for c in s:
            if c == 'I':
                # 要比已使用过的最大的数还要大1
                n = most + 1
                ans[i] = n
                most = n
                i += 1
            else:
                # 要比已使用过的最小的数还要小1
                n = least - 1
                ans[i] = n
                least = n
                i += 1

        # 此时, ans中的都是步长为一个, 需要修正一下.
        shift = min(ans)

        if shift == 0:
            # 正好
            return ans
        elif shift < 0:
            # 每一个元素都要 + abs(shift)
            shift = abs(shift)
            return [e + shift for e in ans]
        else:
            # 每一个元素都要减去shift
            return [e - shift for e in ans]



