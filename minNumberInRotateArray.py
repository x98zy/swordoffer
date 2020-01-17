"""把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。"""
#链接：https://www.nowcoder.com/practice/9f3231a991af4f55b95579b44b7a01ba?tpId=13&tqId=11159&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        start = 0
        end = len(rotateArray) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if rotateArray[mid] > rotateArray[mid + 1]:
                return rotateArray[mid + 1]
            if rotateArray[mid - 1] > rotateArray[mid]:
                return rotateArray[mid]
            if rotateArray[0] < rotateArray[mid]:
                start = mid + 1
            if rotateArray[mid] < rotateArray[end]:
                end = mid - 1
"""算法分析：此处采用的是二分法求解旋转数组的最小值，当rotateArray[mid]>rotateArray[mid+1]或者rotateArray[mid-1]>rotateArray[mid-1]
>rotateArray[mid]时说明已经找到相应的最小值，因为整个数组分成两段来看分别也是递增的，只有过渡到最小值的时候才会出现递减的情况，如数组
[5,6,2,3,4]中[5,6]是递增的，[2,3,4]也是递增的，只有从6到2的时候才出现递减，[4,5,6,2,3]也是如此，只不过对应了两种不同情况。因此整个算法的思想
就是在整个序列中找到递减的序列，此算法的时间复杂度为O(logN),因为 mid = start + (end - start) // 2这一语句是执行的最多的为logN次，当然本例
可以直接用sort方法排序得出结果"""
