'''
这题是一个模拟题, 因为要找能组成的最好的. 就是将从好到坏的规则依次应用在牌中, 第一个应用成功的就是好的.

这题的checkThreeOfAKind和checkPair可以优化一下, 比如提取出共同的部分, 但这里为了代码的美观就不优化了.
'''
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:

        # 这里其实指定了优先顺序, 这个规则应该放在一个单独的地方, 这样就容易使用更改规则了, 而且也更容易看的清.
        if self.checkFlush(suits):
            return "Flush"
        elif self.checkThreeOfAKind(ranks):
            return "Three of a Kind"
        elif self.checkPair(ranks):
            return "Pair"
        else:
            return "High Card"


    def checkFlush(self, suits: List[str]) -> bool:
        return len(set(suits)) == 1


    def checkThreeOfAKind(self, ranks: List[int]) -> bool:
        '''
        判断是否至少有三张大小相同的
        一种方法就是直观的统计, 找是否三张大小相同的.
        另一种就是找一个等价的条件, 即至少三张大小相同的会等价于另一个条件, 而该条件更容易判断.

        '''
        counts = Counter(ranks)

        for count in counts.values():
            if count >= 3:
                return True
        
        return False

    def checkPair(self, ranks: List[int]) -> bool:
        counts = Counter(ranks)

        for count in counts.values():
            if count == 2:
                return True
            
        return False