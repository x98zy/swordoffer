"""实现字符串的Z型变换
https://leetcode-cn.com/problems/zigzag-conversion/"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        res=[[] for _ in range(numRows)]
        index=0
        DESC=True
        for num in s:
            if DESC:
               if index==numRows:
                   index=numRows-2
                   res[index].append(num)
                   index-=1
                   DESC=False
               else:
                   res[index].append(num)
                   index+=1
            else:
                if index==-1:
                    index=1
                    res[index].append(num)
                    index+=1
                    DESC=True
                else:
                    res[index].append(num)
                    index-=1
        ans=""
        for val in res:
            temp="".join(val)
            ans+=temp
        return ans