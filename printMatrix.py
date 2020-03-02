"""题目描述：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10."""
#链接：https://www.nowcoder.com/practice/9b4c81a02cd34f76be2659fa0d54342a?tpId=13&tqId=11172&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
#自己的方案
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if len(matrix)<=1:
            return matrix[0]
        il,ir=0,0#左右坐标
        index=[]#存储已经查找过的坐标
        res=[]#最终结果
        right,left=True,False#z增加或者减少的标志
        length=len(matrix)*len(matrix[0])
        while len(index)<length:
            if right:
                while (il,ir) not in index and ir<len(matrix[0]):
                    res.append(matrix[il][ir])
                    index.append((il,ir))
                    ir+=1
                right,left=False,True
                il+=1
                ir-=1
            if left:
                while (il,ir) not in index and il<len(matrix):
                    res.append(matrix[il][ir])
                    index.append((il,ir))
                    il+=1
                left=False
                ir-=1
                il-=1
            if not right:
                while (il,ir) not in index and ir>=0:
                    res.append(matrix[il][ir])
                    index.append((il,ir))
                    ir-=1
                right=True
                il-=1
                ir+=1
            if not left:
                while (il,ir) not in index and il>=0:
                    res.append(matrix[il][ir])
                    index.append((il,ir))
                    il-=1
                left=True
                ir+=1
                il+=1
        return res
#最佳解答
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if len(matrix)==1:
            return matrix[0]
        if len(matrix)==0:
            return []
        up,down=0,len(matrix)-1
        left,right=0,len(matrix[0])-1
        res=[]
        while True:
            for col in range(left,right+1):
                res.append(matrix[up][col])
            up+=1
            if up>down:
                break
            for col in range(up,down+1):
                res.append(matrix[col][right])
            right-=1
            if left>right:
                break
            for col in range(right,left-1,-1):
                res.append(matrix[down][col])
            down-=1
            if up>down:
                break
            for col in range(down,up-1,-1):
                res.append(matrix[col][left])
            left+=1
            if left>right:
                break
        return res