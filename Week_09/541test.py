#!/usr/bin/env python      
# -*- coding: utf-8 -*-
#541.反转字符串II
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n=len(s)
        t=""
        while n>0:
            if n>=2*k:
                t=t+s[:k][::-1]+s[k:2*k]
                s=s[2*k:]
                n=len(s)
            elif n>k:
                t=t+s[:k][::-1]+s[k:]
                n=0
            else:
                t=t+s[::-1]
                n=0
        return t