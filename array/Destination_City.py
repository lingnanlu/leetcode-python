'''
这题好像就是要找出度为0的城市.
大概思路就是
1. 先统计出所有城市
2. 计算每个城市的出度
3. 再找出度为0的城市
'''
class First:
    def destCity(self, paths: List[List[str]]) -> str:
        cityOut = dict()

        # 先统计所有城市
        for path in paths:
            cityOut[path[0]] = 0
            cityOut[path[1]] = 0

        # 计算每个城市出度
        for path in paths:
            cityOut[path[0]] += 1

        for city, out in cityOut.items():
            if out == 0:
                return city
'''
一种新的方式
'''
class First:
    def destCity(self, paths: List[List[str]]) -> str:
        cityOut = dict()

        # 计算每个城市出度
        for a, b in paths:
            cityOut[a] += 1

        for _, b in paths:
            if cityOut[b] == 0:
                return b


