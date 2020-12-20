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

def InsertSort(iters):
    """插入排序"""
    for i in range(1,len(iters)):
        temp=iters[i]
        j=i-1
        while j>=0 and iters[j]>temp:
            iters[j+1]=iters[j]
            j-=1
        iters[j+1]=temp
    return iters

def ShellSort(iters):
    """希尔排序"""
    space=len(iters)//2
    while space>=1:
        ShellInsert(iters,len(iters),space)
        space=space//2
    return iters
def ShellInsert(iters,length,space):
    for i in range(space,length):
        temp=iters[i]
        j=i-space
        while j>=0 and iters[j]>temp:
            iters[j+space]=iters[j]
            j=j-space
        iters[j+space]=temp


def SelectSort(nums):
    for i in range(len(nums)-1):
        midindex=i
        for j in range(i+1,len(nums)):
            if nums[j]<nums[midindex]:
                midindex=j
        if i!=midindex:
            nums[i],nums[midindex]=nums[midindex],nums[i]
    return nums

def Quick_Sort(nums):
    if len(nums)>=2:
        mid=nums[len(nums)//2]
        left,right=[],[]
        nums.remove(mid)
        for num in nums:
            if num<mid:
                left.append(num)
            else:
                right.append(num)
        return Quick_Sort(left)+[mid]+Quick_Sort(right)
    else:
        return nums

print(Quick_Sort([2,4,1,7,5,3,9]))


#堆排序
def buildmaxheap(arr):
    """构建大顶堆"""
    for i in range(len(arr)//2,-1,-1):
        heapify(arr,i)

def heapify(arr,i):
    """确保根节点最大"""
    left=2*i+1
    right=2*i+2
    largest=i
    if left<arrlen and arr[left]>arr[largest]:
        largest=left
    if right<arrlen and arr[right]>arr[largest]:
        largest=right

    if largest!=i:
        swap(arr,i,largest)
        heapify(arr,largest)

def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]

def heapsort(arr):
    global arrlen
    arrlen=len(arr)
    buildmaxheap(arr)
    for i in range(len(arr)-1,0,-1):
        swap(arr,0,i)
        arrlen-=1
        heapify(arr,0)

    return arr

def CountingSort(arr):
    max_value=max(arr)
    bucket_len=max_value+1
    bucket=[0]*bucket_len

    for i in range(len(arr)):
        if not bucket[arr[i]]:
            bucket[arr[i]]=0
        bucket[arr[i]]+=1

    sortindex=0
    for j in range(bucket_len):
        while bucket[j]>0:
            arr[sortindex]=j
            sortindex+=1
            bucket[j]-=1
    return arr


print(CountingSort([1,4,2,7,5,11,9]))
