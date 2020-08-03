def MaoPaoSort(iters=None):
    """冒泡算法"""
    flag=False
    for i in range(len(iters)-1,0,-1):
        if flag==True:
            break
        flag=True
        for j in range(0,i):
            if iters[j]<iters[j+1]:
                iters[j],iters[j+1]=iters[j+1],iters[j]
                flag=False
    return iters

def MaoPaoSort1(iters):
    low,high=0,len(iters)-1
    while low<high:
        for i in range(0,high):
            """正向冒泡寻求最小值"""
            if iters[i]<iters[i+1]:
                iters[i],iters[i+1]=iters[i+1],iters[i]
        high-=1
        for j in range(high,low,-1):
            """反向冒泡寻求最大值"""
            if iters[j]>iters[j-1]:
                iters[j],iters[j-1]=iters[j-1],iters[j]
        low+=1
    return iters

print(MaoPaoSort1([1,3,2,7,4,6,9]))
