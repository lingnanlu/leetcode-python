'''
这题按照题意, 其实就是要根据每人个的得分知道其名次.
而怎么知道名次呢? 名次其实和排序有关.

排完序之后, 要从左到右遍历. 要快速的知道某人名次
'''
from typing import List


class First:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_copy = score.copy()

        score_copy.sort(reverse=True)

        rand = dict()

        for i, v in enumerate(score_copy):
            rand[v] = i + 1

        ans = []

        for s in score:
            if rand[s] == 1:
                ans.append("Gold Medal")
            elif rand[s] == 2:
                ans.append("Silver Medal")
            elif rand[s] == 3:
                ans.append("Bronze Medal")
            else:
                ans.append(str(rand[s]))

        return ans





