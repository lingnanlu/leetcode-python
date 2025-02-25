'''
这题的关键就在于，如何快速判断一个单词中的所有字母是否在同一行。

最直观的作法就是，对于某单词的每个字母，从前往后依次判断是否在同一行。

这就需要能快速判断某个字母是否属于某一行。这个操作的复杂度应该为1

在python中，使用集合就可以快速判断某个字母是否属于这个集合，时间复杂度为O(1)

'''

class Solution:

    first_row = set('qwertyuiop')
    second_row = set('asdfghjkl')
    third_row = set('zxcvbnm')

    def findWords(self, words: List[str]) -> List[str]:
    
        result = []

        for word in words:
            # 这里就是判断word中的每个字母是否在同一行
            
            