#!/usr/bin/env pytho      
# -*- coding: utf-8 -*-
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp=[]
        # j = len(nums)-1
        # while nums[j]> target:
        #     j = j-1
        #     if j <= 0:
        #         return
        for i in range(0,len(nums)-1):
            for k in range(i+1,len(nums)):
                if nums[i]+nums[k]==target:
                    temp=[i,k]
        return temp