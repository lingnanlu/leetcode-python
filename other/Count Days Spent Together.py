'''
日期其实是一个区间，其实这题有点感觉像找两个区间的交集。
一种方法就是真的把两个区间变成集合，这是可以的，因为日期是离散的，然后两找交集。
另一种其实就是数学的方法，其实就是找到交集的两个界限，然后计算这个区间中的天数。

本题写的时候最容易出错的地方,就是不断的将某个子串当成月或天.
不如先把字符串转化成结构化的月和日,再计算也不错.
'''
dayOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # 先判断两者有没有交集.这个要形象的想像一下在数轴上的样子.
        # 两种情况, alice的离开时间早于bob的到达时间,或者bob的离开时间早于alice的到达时间.
        if leaveAlice < arriveBob or leaveBob < arriveAlice:
            return 0
        else:
            # 找到两者边界
            arriveLast = max(arriveAlice, arriveBob)
            leaveFirst = min(leaveAlice, leaveBob)

            days = 0
            # 两者的边界之间的日期包含两种, 一种是完整月, 一种是不完整月. 分别统计
            for i in range(int(arriveLast[0:2]) + 1, int(leaveFirst[0:2])):
                days += dayOfMonth[i - 1]

            if arriveLast[0:2] == leaveFirst[0:2]: #说明是同一个月
                days += int(leaveFirst[3:5]) - int(arriveLast[3:5]) + 1
            else:
                days += dayOfMonth[arriveLast[0:2] - 1] - int(arriveLast[3:5]) + 1
                days += int(leaveFirst[3:5])

            return days