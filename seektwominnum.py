"""寻求一个数组中最小的两个数"""

def seekmintwonum(arr):
    min1,min2=float("INF"),float("INF")
    for num in arr:
        if num<min1:
            min2=min1
            min1=num
        elif num<min2:
            min2=num
    return min1,min2

if __name__=="__main__":
    print(seekmintwonum([6,5,7,1,2,9]))