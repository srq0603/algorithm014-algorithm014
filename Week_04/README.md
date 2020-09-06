学习笔记
第4周总结
1.使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方
思路:初始值left=arr[0],right=arr[len(arr)-1],当left<=right时，mid=(left+right)/2,
如果arr[mid]>right,left=mid,如果arr[mid]<left,right=mid,如果left+1=right,则返回left，right的值
即为中间无序的地方
2.贪心算法适用于处理找最优解得问题，根据题目找到一些规律，简化求解过程，从而找到最优解