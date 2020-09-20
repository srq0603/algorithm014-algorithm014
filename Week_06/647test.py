#!/usr/bin/env python      
# -*- coding: utf-8 -*-
#647.回文子串
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        dp = [[0] for _ in range(len(s))]
        for j in range(len(s)):
            for i in range (0,j+1):
                if i == j:
                    dp[i] = True
                    count += 1
                elif i == j-1 and s[i] == s[j]:
                    dp[i] = True
                    count += 1
                elif j-i >1 and s[i] == s[j] and dp[i+1]:
                    dp[i] = True
                    count += 1
                else:
                    dp[i] = False
        return count