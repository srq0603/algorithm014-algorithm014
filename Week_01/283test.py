#!/usr/bin/env pytho      
# -*- coding: utf-8 -*-
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(0,len(nums)):
            if nums[i]!=0:
                nums[j]=nums[i]
                j = j+1
        for k in range(j,len(nums)):
            nums[k]=0
        return nums