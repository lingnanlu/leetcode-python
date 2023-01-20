
'''
其实就是翻译, 然后使用集合去重
'''

MORSE = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

class First:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        translated = set()
        for word in words:
            # 对每一个单词进行翻译, 这本要字符串连接
            s = ""
            for c in word:
                s += MORSE[ord(c) - ord('a')]
            translated.add(s)

        return len(translated)

'''
一种更函数的写法
利用list comprehension
虽然紧凑, 但并不易读
可以想成把一个列表转化成另一个
'''
class Second:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # 利用列表推导, 展开成一个二维的. 然后再把二维变成一维的
        # [(MORSE[ord(c) - ord('a')] for c in word) for word in words]
        return len(set(["".join((MORSE[ord(c) - ord('a')] for c in word)) for word in words]))

