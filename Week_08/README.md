1.冒泡排序
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
2.选择排序
def selectedSort(arr):
    for i in range(len(arr)):
          min = i
          for j in range(i+1,len(arr)):
              if arr[j]<arr[min]:
                  min = j
          arr[i], arr[min] = arr[min], arr[i]
    return arr
3.插入排序
def insertionSort(arr):
     for i in range(1,len(arr)):
         preIndex = i-1
         current = arr[i]
         #从已排序的数组最后一个元素开始比较，依次向前，找到位置后插入
          while preIndex>=0 and arr[preIndex]>current:
              arr[preIndex+1] = arr[preIndex]
              preIndex -= 1
          arr[preIndex+1] = current
     return arr
4.快速排序
def quickSort(arr,start,end):
      if start<end:
          #i,j指针指向数组起始位置
          i, j = start, end
          key = arr[i]
          while i<j:
              #小于key时，交换到前面
              while i<j and arr[j]>=key:
                  j -= 1
              arr[i] = arr[j]
              while i<j and arr[i]<=key:
                  i += 1
              arr[j] = arr[i]
          #将中间的数替换为key
          arr[i] = key
          #递归调用
          quickSort(arr,start,i-1)
          quickSort(arr,j+1,end)
      return arr    