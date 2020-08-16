#!/usr/bin/env pytho      
# -*- coding: utf-8 -*-
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        k = k % len(nums)

        temp = nums[len(nums) - k:]
        nums[k:] = nums[:len(nums) - k]
        nums[:k] = temp
        return