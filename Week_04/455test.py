#!/usr/bin/env python      
# -*- coding: utf-8 -*-
#分发饼干
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g1 = sorted(g)
        s1 = sorted(s)
        print(g)
        print(s)
        child = 0
        i = j = 0
        while i < len(g1) and j <len(s1):
            while i< len(g1) and j<len(s1) and g1[i]<=s1[j]:
                i += 1
                j += 1
                child +=1
            while i<len(g1) and j<len(s1) and g1[i]>s1[j]:
                j += 1
        return child


