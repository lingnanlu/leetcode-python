'''
如果我们不考虑names的话, 只排序身高可以使用内置函数
但身高原来的下标是有意义的, 这个下标对应着名字.
所以, 我们要通过身高,得到原来的下标,再得到名字.
其实, 最终目标就是通过身高得到名字.
那么, 先建立一个映射就好.
'''
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heigh2name = dict(zip(heights, names))

        sortedHeights = sorted(heights, reverse = True)

        sortedNames = []

        for height in sortedHeights:
            sortedNames.append(heigh2name[height])
        
        return sortedNames