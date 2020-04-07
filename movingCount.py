"""题目描述
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k
的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？"""

#链接：https://www.nowcoder.com/practice/6e5207314b5241fb83f2329e89fdecc8?tpId=13&tqId=11219&tPage=4&rp=4&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    def __init__(self):
        self.dict={}
        self.count=0
    def get_sum(self,i,j):
        num=0
        while i:
            num+=i%10
            i=i//10
        while j:
            num+=j%10
            j=j//10
        return num
    def dfs(self,matrix,i,j,k):
        if not (0<=i<len(matrix) and 0<=j<len(matrix[0])):
            return
        if self.dict.get((i,j)) is not None:
            return
        if self.get_sum(i,j)>k:
            return
        self.dict[(i,j)]=1
        self.count+=1
        self.dfs(matrix,i+1,j,k)
        self.dfs(matrix,i,j+1,k)
        self.dfs(matrix,i-1,j,k)
        self.dfs(matrix,i,j-1,k)
    def movingCount(self, threshold, rows, cols):
        # write code here
        matrix=[[1 for i in range(cols)] for j in range(rows)]
        self.dfs(matrix,0,0,threshold)
        return self.coun
