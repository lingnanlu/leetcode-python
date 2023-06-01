# 其实这题的意思就是比较s中的两个相同的字母之间的距离是不是和distance中的一样.
class First:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        first = [-1] * 26 # 记录第一次出现的位置
        second = [-1] * 26 # 记录第二次出现的位置


        for index, value in enumerate(s):
            code = ord(value) - ord('a')
            if first[code] == -1:
                first[code] = index
            else:
                second[code] = index
                if second[code] - first[code] - 1 != distance[code]:
                    return False
                
        return True
        
