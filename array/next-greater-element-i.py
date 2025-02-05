'''
a more simple question is nums1 is a number not an list.
to solve this problem, you just need to traverse nums2.

if nums1 is a list, just loop nums1 and each loop is the question above.

对于每一个nums1中的元素，都要在nums2中去寻找其位置。
也就是说，nums2中的元素需要从前往后遍历多次。这是浪费时间的。
不知先遍历一次nums2中的元素，将nums1中的元素定位这个操作变成O(1)
然后再去找第一个比它大的元素。

当然，这个优化的前提是当nums1中的元素比较多时，才这样做，如果比较少，遍历nums2就不合算了。


'''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        result = []
        num2index = {num: i for i, num in enumerate(nums2)}

        for num in nums1:
            
            index = num2index[num]

            for i in range(index + 1, len(nums2)):
                if nums2[i] > num:
                    result.append(nums2[i])
                    break
            else:
                result.append(-1)
        
        return result
