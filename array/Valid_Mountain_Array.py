'''
判断是不是有效的山脉数组, 其实就按照题意, 一项一项的检查就行
全部检查通过了, 就是, 如果有一项没通过, 就不是
'''
class First:
    def validMountainArray(self, arr: List[int]) -> bool:

        # 第一个条件.
        if len(arr) < 3:
            return False

        # 存在一个连续上坡

        i = 0
        while i <= len(arr) - 2:
            if arr[i] < arr[i + 1]:
                i += 1
            else:
                break



        # 此时, i = len(arr) - 1, 即最后一个, 或 arr[i] >= arr[i + 1]

        # 说明没有上坡
        if i == 0:
            return False

        # 说明只有上坡, 没有下坡
        if i == len(arr) - 1:
            return False

        # 到了这里有上坡, 看剩余的应该都是下坡了
        while i <= len(arr) - 2:
            if arr[i] > arr[i + 1]:
                i += 1
            else:
                break

        # 剩下的不全是下坡, 还有元素
        if i != len(arr) - 1:
            return False

        # 到此, 条件全部通过.
        return True
