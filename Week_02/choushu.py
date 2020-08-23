#!/usr/bin/env python      
# -*- coding: utf-8 -*-
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1]*n
        a = b = c = 0
        for i in range(1,n):
           n2 = dp[a]*2
           n3 = dp[b]*3
           n5 = dp[c]*5
           dp[i] = min(n2,n3,n5)
           if dp[i] ==n2: a+=1
           if dp[i] ==n3: b+=1
           if dp[i] ==n5: c+=1
        return dp[-1]